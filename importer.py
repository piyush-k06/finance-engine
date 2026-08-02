from transaction import add_transaction, transaction_exists
import pandas as pd
from pathlib import Path
from config.column_map import COLUMN_MAP
from config.category_rules import CATEGORY_RULES

def load_file(path: Path):
    path = str(path).lower()
    if path.endswith(".csv"):
        return pd.read_csv(path)
    elif path.endswith(".xlsx"):
        return pd.read_excel(path, engine="openpyxl")
    else:
        raise ValueError("Unsupported file type")


def map_columns(df):
    cols = {}
    for std, names in COLUMN_MAP.items():
        found = []
        for s in df.columns:
            if s in names:
                found.append(s)
        if len(found) == 0:
            raise ValueError(f"No matching column found for {std}")
        elif len(found) > 1:
            raise ValueError(f"Multiple matching columns found for {std}: {found}")
        cols[found[0]] = std
    df = df.rename(columns=cols)
    return df[list(COLUMN_MAP.keys())]


def clean_data(df):

    df['raw_vendor'] = df['raw_vendor'].astype("string").str.strip()
    df['raw_vendor'] = df['raw_vendor'].replace('', pd.NA)

    df['amount'] = df['amount'].astype("string")
    df['amount'] = df['amount'].str.replace(',', '').str.replace('₹', '').str.strip()
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    df['date'] = df['date'].astype("string").str.strip()
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')

    return df

def validate_data(df):
    errors = []
    duplicates = []
    for i, row in df.iterrows():
        row_errors = []
        if pd.isna(row['date']):
            row_errors.append("Missing date")
        if pd.isna(row['raw_vendor']):
            row_errors.append("Missing vendor")
        if pd.isna(row['amount']):
            row_errors.append("Invalid amount")
        if row_errors:
            errors.append("Row " + str(i + 1) + ": " + ", ".join(row_errors))
    dup = df[df.duplicated(subset=['date', 'raw_vendor', 'amount'], keep=False)]
    if not dup.empty:
        duplicates = dup.index.tolist()
    return errors, duplicates

def categorize_data(df):
    categories = []
    for vendor in df['raw_vendor']:
        if pd.isna(vendor):
                categories.append("Uncategorized")
                continue
        vendor = vendor.lower()
        category = "Uncategorized"
        for keyword, cat in CATEGORY_RULES.items():
            if keyword in vendor:
                category = cat
                break
        categories.append(category)
    df['category_name'] = categories
    return df

def import_transactions(df, duplicate_option="skip"):
    
    imported = 0
    skipped = 0
    for i, row in df.iterrows():
        if (pd.isna(row['date']) or 
            pd.isna(row['raw_vendor']) or 
            pd.isna(row['amount'])
        ):
            continue
        if transaction_exists(row['date'], row['raw_vendor'], row['amount']):
            if duplicate_option == "skip":
                skipped += 1
                continue
            elif duplicate_option == "cancel":
                return {
                    "imported": imported,
                    "skipped": skipped,
                    "status": "cancelled"
                }
            elif duplicate_option == "import_all":
                pass  
        add_transaction(
            row['date'],
            row['raw_vendor'],
            row['amount'],
            row['category_name']
        )
        imported += 1
    return {
        "imported": imported,
        "skipped": skipped,
        "status": "completed"
    }

def import_file(path):
    df = load_file(Path(path))
    df = map_columns(df)
    df = clean_data(df)

    errors, duplicates = validate_data(df)

    if errors:
        print(errors)
        return None

    df = categorize_data(df)

    return import_transactions(df)

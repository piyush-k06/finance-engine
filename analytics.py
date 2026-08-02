import pandas as pd

def total_spending(df):
    return df['amount'].sum()

def category_summary(df):
    return df.groupby('category_name')['amount'].sum().reset_index()

def vendor_summary(df):
    return df.groupby('raw_vendor')['amount'].sum().reset_index()

def monthly_summary(df):
    d = df.copy()
    d['date'] = pd.to_datetime(d['date'])
    d['month'] = d['date'].dt.to_period('M')
    return d.groupby('month')['amount'].sum().reset_index()

def highest_transaction(df):
    if df.empty:
        return None
    return df.loc[df['amount'].idxmax()]

def average_transaction(df):
    return df['amount'].mean()
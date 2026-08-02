from analytics import *
import pandas as pd


def summary_report(
    df,
    total=False,
    average=False,
    highest=False,
    category=False,
    vendor=False,
    monthly=False
):
    report = {}
    if total:
        report['total_spending'] = total_spending(df)
    if average:
        report['average_transaction'] = average_transaction(df)
    if highest:
        report['highest_transaction'] = highest_transaction(df)
    if category:
        report['category_summary'] = category_summary(df)
    if vendor:
        report['vendor_summary'] = vendor_summary(df)
    if monthly:
        report['monthly_summary'] = monthly_summary(df)

    return report


def filter_report(
    df,
    start_date=None,
    end_date=None,
    categories=None,
    vendors=None,
    total=False,
    average=False,
    highest=False,
    category=False,
    vendor=False,
    monthly=False
):
    d = df.copy()

    if start_date or end_date:
        d['date'] = pd.to_datetime(d['date'])
        if start_date:
            start_date = pd.to_datetime(start_date)
            d = d[d['date'] >= start_date]
        if end_date:
            end_date = pd.to_datetime(end_date)
            d = d[d['date'] <= end_date]

    if categories:
        d = d[d['category_name'].isin(categories)]

    if vendors:
        d = d[d['raw_vendor'].isin(vendors)]

    return summary_report(
        d,
        total=total,
        average=average,
        highest=highest,
        category=category,
        vendor=vendor,
        monthly=monthly
    )
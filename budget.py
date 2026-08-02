from reports import filter_report
from db import get_db
import calendar

def set_budget(category, month, amount):
    con, cur = get_db()

    cur.execute(
        "SELECT category_id FROM categories WHERE category_name = ?",
        (category,)
    )
    row = cur.fetchone()

    if not row:
        print("Category not found.")
        return

    category_id = row[0]

    cur.execute(
        "SELECT * FROM budgets WHERE category_id = ? AND month = ?",
        (category_id, month)
    )

    if cur.fetchone():
        print("Budget already exists.")
        return

    cur.execute(
        "INSERT INTO budgets(category_id, month, amount) VALUES (?, ?, ?)",
        (category_id, month, amount)
    )

    con.commit()
    print("Budget added successfully.")





def get_budget(category, month):
    con, cur = get_db()

    cur.execute(
        """
        SELECT b.amount
        FROM budgets b
        JOIN categories c
        ON b.category_id = c.category_id
        WHERE c.category_name = ? AND b.month = ?
        """,
        (category, month)
    )

    row = cur.fetchone()

    if row:
        return row[0]

    return None





def update_budget(category, month, amount):
    con, cur = get_db()

    cur.execute("""
        UPDATE budgets
        SET amount = ?
        WHERE category_id = (
            SELECT category_id
            FROM categories
            WHERE category_name = ?
        )
        AND month = ?
    """, (amount, category, month))

    con.commit()

    if cur.rowcount:
        print("Budget updated successfully.")
    else:
        print("Budget not found.")





def delete_budget(category, month):
    con, cur = get_db()

    cur.execute("""
        DELETE FROM budgets
        WHERE category_id = (
            SELECT category_id
            FROM categories
            WHERE category_name = ?
        )
        AND month = ?
    """, (category, month))

    con.commit()

    if cur.rowcount:
        print("Budget deleted successfully.")
    else:
        print("Budget not found.")





def budget_summary(df, category, month):
    budget = get_budget(category, month)

    if budget is None:
        return None

    year = int(month[:4])
    mon = int(month[5:])
    last_day = calendar.monthrange(year, mon)[1]

    spending = filter_report(
        df,
        start_date=f"{month}-01",
        end_date=f"{month}-{last_day:02d}",
        categories=[category],
        total=True
    )

    spent = float(spending.get('total_spending', 0))
    remaining = float(budget - spent)

    return {
        "category": category,
        "month": month,
        "budget": budget,
        "spent": spent,
        "remaining": remaining,
        "status": "Within Budget" if remaining >= 0 else "Exceeded"
    }





def budget_alerts(df, month):
    con, cur = get_db()

    cur.execute("""
        SELECT c.category_name
        FROM budgets b
        JOIN categories c
        ON b.category_id = c.category_id
        WHERE b.month = ?
    """, (month,))

    rows = cur.fetchall()

    alerts = []

    for row in rows:
        summary = budget_summary(df, row[0], month)

        if summary and summary['remaining'] < 0:
            alerts.append(summary)

    return alerts
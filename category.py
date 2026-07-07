def get_category_id(cur, category_name):
    cur.execute("SELECT category_id FROM categories WHERE category_name=?", (category_name,))
    category_id = cur.fetchone()
    if category_id:
        return category_id[0]
    return None
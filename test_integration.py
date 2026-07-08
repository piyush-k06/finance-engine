from transaction import add_transaction

# existing vendor

add_transaction(
    "2026-07-08",
    "AMZN",
    500,
    "Shopping"
)

# new vendor

add_transaction(
    "2026-07-08",
    "Gupta Store",
    230,
    "Food"
)

# duplicate vendor

add_transaction(
    "2026-07-08",
    "Gupta Store",
    230,
    "Food"
)

# invalid category

add_transaction(
    "2026-07-08",
    "AMZN",
    500,
    "Shoppinggg"
)
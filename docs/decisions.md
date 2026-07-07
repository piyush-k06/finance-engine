# Design Decisions

## Categories are fixed

Decision

Users cannot create categories.

Reason

Allowing custom categories creates inconsistent analytics.

Example:

Food
Foods
FOOD

Future

Custom categories may be added later if required.

---

## Vendors are dynamic

Decision

Unknown vendors are created automatically.

Reason

New vendors appear every day.

Example:

Amazon
Local Grocery Store
Uber

---

## Vendor aliases

Decision

Store raw names separately from canonical vendors.

Reason

Different banks may represent the same vendor differently.

Example:

AMZN

Amazon

Amazon Pay

---

## Commit ownership

Decision

Only transaction.py performs database commits.

Reason

Ensures atomic transactions.

Problem solved

Multiple commits and partial database updates.

---

## Category validation

Decision

Reject transactions with invalid categories.

Reason

Bad data is worse than missing data.
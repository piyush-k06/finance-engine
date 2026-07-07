# Interview Notes

## Foreign Keys

Purpose

Maintain relationships between tables.

Used In

transactions

vendor_aliases

---

## Normalization

Purpose

Reduce duplicate data.

Used In

Separate vendors and aliases.

---

## Atomic Transactions

Definition

A transaction should either complete fully or not execute at all.

Used In

transaction.py owns commit.

---

## Idempotency

Definition

Executing the same operation multiple times should not create duplicate data.

Example

Calling get_vendor_id("AMZN") repeatedly.

---

## Modular Architecture

Definition

Each module has one responsibility.

Modules

vendor.py

category.py

transaction.py
import csv
import os

FILE_NAME = "expenses.csv"
HEADERS = ["ID", "Date", "Description", "Amount"]


def load_expenses():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS)
            writer.writeheader()
    with open(FILE_NAME, "r") as f:
        try:
            reader = csv.DictReader(f)
            return list(reader)
        except csv.Error:
            return []


def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(expenses)

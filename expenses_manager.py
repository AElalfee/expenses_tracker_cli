from storage import load_expenses, save_expenses
from datetime import date


def add_expenses(amount: float, description: str):
    next_id = 1
    expenses = load_expenses()
    if expenses:
        next_id = max(int(expense["ID"]) for expense in expenses) + 1
    expense = {
        "ID": next_id,
        "Date": date.today(),
        "Description": description,
        "Amount": f"AED {amount}",
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expenses added successfully (ID: {expense['ID']})")


def get_expenses():
    return load_expenses()


def get_expense_by_id(id: int):
    expenses = load_expenses()
    return [expense for expense in expenses if int(expense["ID"]) == id]

from storage import load_expenses, save_expenses
from datetime import date


def add_expenses(description: str, amount: float):
    next_id = 1
    expenses = load_expenses()
    if expenses:
        next_id = max(expenses["ID"] for expense in expenses) + 1
    expense = {
        "ID": next_id,
        "Date": date.today(),
        "Description": description,
        "Amount": f"AED {amount}",
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expenses added successfully (ID: {expense['ID']})")

from storage import load_expenses, save_expenses
from datetime import date, datetime


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


def update_expenses(id: int, amount: float = None, description: str = None):
    expenses = load_expenses()
    for expense in expenses:
        if int(expense["ID"]) == id:
            if amount:
                expense["Amount"] = amount
            if description:
                expense["Description"] = description
            save_expenses(expenses)


def delete_expenses(id: int):
    expenses = load_expenses()
    expenses = [expense for expense in expenses if int(expense["ID"]) != id]
    save_expenses(expenses)


def summary(month: int = None):
    total = 0
    expenses = load_expenses()
    current_year = date.today().year

    if month is None:
        for expense in expenses:
            if (
                datetime.strptime(expense["Date"], "%Y-%m-%d").date().year
                == current_year
            ):
                total = total + float(expense["Amount"].replace("AED ", ""))
        return f"Total Expenses: AED {total}"

    for expense in expenses:
        if (
            datetime.strptime(expense["Date"], "%Y-%m-%d").date().year == current_year
            and datetime.strptime(expense["Date"], "%Y-%m-%d").date().month == month
        ):
            total = total + float(expense["Amount"].replace("AED ", ""))
    return f"Total Expenses: AED {total}"

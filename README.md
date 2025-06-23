
# Expense Tracker CLI

A simple expense tracker application to manage your finances. The application should allow users to add, delete, and view their expenses. The application should also provide a summary of the expenses.


<a href="https://roadmap.sh/projects/expense-tracker" target="_blank">
<img src="preview.gif" alt="Preview">
</a>

## Features

- Add an expense with a description and amount.
- Update an expense.
- Delete an expense.
- View all expenses.
- View summary of all expenses.
- View a summary of expenses for a specific month (of current year).


## Project Structure

- **main.py**: main file (CLI Entrypoint) 
- **expenses_manager.py**: Contains core functions
- **storage.py**: Handles CSV loading & saving
- **utils.py**: Contains helper functions
- **tests.py**: Contains test cases for core functions
## Installation

Make sure you have Python 3 installed.

**Clone the repository**:

```bash
  git clone https://github.com/AElalfee/expenses_tracker_cli.git
  cd expenses_tracker_cli
```
    
## Usage/Examples

- **Add expense**:

```bash
python3 main.py add --amount 13.00 --description Lunch

Expenses added successfully (ID: 1)
```

- **List expenses**:

```bash
python3 main.py list

[{'ID': '1', 'Date': '2025-06-24', 'Description': 'Lunch', 'Amount': 'AED 13.0'}]
```

- **Summary**:

```bash
python3 main.py summary

Total Expenses: AED 13.0
```

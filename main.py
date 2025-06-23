import argparse

from expenses_manager import (
    add_expenses,
    get_expenses,
    update_expenses,
    delete_expenses,
    summary,
)


def main():
    parser = argparse.ArgumentParser(
        prog="expense-tracker",
        usage="python3 main.py [options]",
        description="A simple expense tracker application to manage your finances. The application should allow users to add, delete, and view their expenses. The application should also provide a summary of the expenses.",
        epilog="For more information, visit https://github.com/AElalfee/expenses_tracker_cli",
    )

    subparser = parser.add_subparsers(dest="command", required=True)

    parser_add = subparser.add_parser("add", help="Add expenses")
    parser_add.add_argument(
        "--amount", type=float, required=True, help="Amount of expense"
    )
    parser_add.add_argument(
        "--description", type=str, required=True, help="Description of expense"
    )

    parser_update = subparser.add_parser("update", help="Update expense")
    parser_update.add_argument("--id", type=int, required=True, help="ID of expense")
    parser_update.add_argument(
        "--amount", type=float, default=None, required=False, help="Amount of expense"
    )
    parser_update.add_argument(
        "--description",
        type=str,
        default=None,
        required=False,
        help="Description of expense",
    )

    parser_delete = subparser.add_parser("delete", help="Delete expense")
    parser_delete.add_argument("--id", type=int, required=True, help="ID of expense")

    parser_list = subparser.add_parser("list", help="List expenses")

    parser_summary = subparser.add_parser(
        "summary", help="Get total amount of expenses."
    )
    parser_summary.add_argument(
        "--month", type=int, default=None, help="Month you to get summary of"
    )

    args = parser.parse_args()

    if args.command == "add":
        add_expenses(args.amount, args.description)
    elif args.command == "list":
        print(get_expenses())
    elif args.command == "summary":
        summary(args.month)
    elif args.command == "update":
        update_expenses(args.id, args.amount, args.description)
    elif args.command == "delete":
        delete_expenses(args.id)


if __name__ == "__main__":
    main()

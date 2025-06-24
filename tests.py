import unittest

from expenses_manager import (
    get_expenses,
    delete_expenses,
    add_expenses,
    update_expenses,
)
from utils import get_amount


class TestExample(unittest.TestCase):
    def setUp(self):
        self.amount = 13.00
        self.description = "Lunch"
        self.new_description = "Dinner"
        self.expense_id = None

        for expense in get_expenses():
            delete_expenses(int(expense["ID"]))
        if self._testMethodName != "test_add_expenses":
            add_expenses(self.amount, self.description)
            expense = next(
                e for e in get_expenses() if e["Description"] == self.description
            )
            self.expense_id = int(expense["ID"])

    def tearDown(self):
        for expense in get_expenses():
            delete_expenses(int(expense["ID"]))

    def test_add_expenses(self):
        add_expenses(self.amount, self.description)
        expenses = get_expenses()
        self.assertIn(
            self.description, [expense["Description"] for expense in expenses]
        )
        self.assertIn(
            self.amount, [get_amount(expense["Amount"]) for expense in expenses]
        )

    def test_update_expenses(self):
        update_expenses(self.expense_id, description=self.new_description)
        expenses = get_expenses()
        self.assertIn(
            self.new_description, [expense["Description"] for expense in expenses]
        )

    def test_delete_expenses(self):
        delete_expenses(self.expense_id)
        expenses = get_expenses()
        self.assertNotIn(
            self.description, [expense["Description"] for expense in expenses]
        )

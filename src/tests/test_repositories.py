import unittest
import sqlite3
from repositories.budget_repository import BudgetRepository
from repositories.user_repository import UserRepository

class TestRepositories(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row

        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE users (username TEXT PRIMARY KEY, password TEXT)")
        cursor.execute("CREATE TABLE expenses (id INTEGER PRIMARY KEY, amount INTEGER, category TEXT, user_id TEXT REFERENCES users)")
        self.connection.commit()

        self.budget_repo = BudgetRepository(self.connection)
        self.user_repo = UserRepository(self.connection)

    def test_user_create_and_find(self):
        self.user_repo.create("steffe", "nissinen123")
        user = self.user_repo.find_by_username("steffe")
        
        self.assertEqual(user["username"], "steffe")
        self.assertEqual(user["password"], "nissinen123")

    def test_find_non_existent_user(self):
        user = self.user_repo.find_by_username("haamu")
        self.assertIsNone(user)

    def test_expense_create_and_find_all(self):
        self.user_repo.create("steffe", "nissinen123")
        self.budget_repo.create(150, "ruoka", "steffe")
        self.budget_repo.create(50, "bensa", "steffe")
        
        expenses = self.budget_repo.find_all("steffe")
        
        self.assertEqual(len(expenses), 2)
        self.assertEqual(expenses[0]["amount"], 150)
        self.assertEqual(expenses[1]["category"], "bensa")

    def test_expense_delete(self):
        self.user_repo.create("steffe", "nissinen123")
        self.budget_repo.create(150, "ruoka", "steffe")
        
        expenses = self.budget_repo.find_all("steffe")
        expense_id = expenses[0]["id"]

        self.budget_repo.delete(expense_id)
        remaining = self.budget_repo.find_all("steffe")
        self.assertEqual(len(remaining), 0)

    def test_expense_update(self):
        self.user_repo.create("steffe", "nissinen123")
        self.budget_repo.create(100, "vanha", "steffe")
        expenses = self.budget_repo.find_all("steffe")
        expense_id = expenses[0]["id"]
        self.budget_repo.update(expense_id, 200, "uusi")

        updated = self.budget_repo.find_all("steffe")
        self.assertEqual(updated[0]["amount"], 200)
        self.assertEqual(updated[0]["category"], "uusi")
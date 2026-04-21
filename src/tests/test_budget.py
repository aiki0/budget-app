import unittest
from services.budget_service import BudgetService


class FakeBudgetRepository:
    def __init__(self, expenses=None):
        self.expenses = expenses or []
        self._id_counter = 1

    def find_all(self, user_id):
        user_expenses = filter(
            lambda expense: expense["user_id"] == user_id,
            self.expenses
        )
        return list(user_expenses)

    def create(self, amount, category, user_id):
        expense = {
            "id": self._id_counter,
            "amount": amount,
            "category": category,
            "user_id": user_id
        }
        self.expenses.append(expense)
        self._id_counter += 1
        return expense

    def delete(self, expense_id):
        expenses_without_id = filter(
            lambda expense: expense["id"] != expense_id,
            self.expenses
        )
        self.expenses = list(expenses_without_id)


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_by_username(self, username):
        matching_users = filter(
            lambda user: user["username"] == username,
            self.users
        )
        matching_users_list = list(matching_users)
        return matching_users_list[0] if len(matching_users_list) > 0 else None

    def create(self, username, password):
        user = {"username": username, "password": password}
        self.users.append(user)
        return user



class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.service = BudgetService(
            FakeBudgetRepository(),
            FakeUserRepository())
        self.test_user = "matti"
        self.test_pass = "matti123"

    def login_user(self):
        self.service.register(self.test_user, self.test_pass)
        self.service.login(self.test_user, self.test_pass)

    def test_register_and_login(self):
        self.service.register(self.test_user, self.test_pass)
        user_ok = self.service.login(self.test_user, self.test_pass)
        
        self.assertTrue(user_ok)
        self.assertEqual(self.service._user["username"], self.test_user)

    def test_login_with_invalid_password(self):
        self.service.register(self.test_user, self.test_pass)
        user_ok = self.service.login(self.test_user, "vaara_passu")
        self.assertFalse(user_ok)

    def test_create_expense(self):
        self.login_user()
        self.service.add_expense(100, "ruoka")
        
        expenses = self.service.get_all()
        self.assertEqual(len(expenses),1)
        self.assertEqual(expenses[0]["amount"], 100)
        self.assertEqual(expenses[0]["category"], "ruoka")

    def test_create_expense_invalid_amount(self):
        self.login_user()
        result = self.service.add_expense(-10, "virhe")
        self.assertFalse(result)

    def test_delete_expense(self):
        self.login_user()
        self.service.add_expense(50, "leffa")
        
        expenses = self.service.get_all()
        expense_id = expenses[0]["id"]
        
        self.service.delete_expense(expense_id)
        
        remaining_expenses = self.service.get_all()
        self.assertEqual(len(remaining_expenses), 0)

    def test_get_all_without_login(self):
        expenses = self.service.get_all()
        self.assertEqual(expenses, [])

    def test_register_existing_user(self):
        self.service.register(self.test_user, self.test_pass)
        result = self.service.register(self.test_user, "toinen_passu")
        self.assertFalse(result)
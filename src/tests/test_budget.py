import unittest
from services.budget_service import BudgetService

class FakeRepository:
    def __init__(self):
        self.expenses = []
    def create(self, amount, category):
        self.expenses.append((amount, category))
    def find_all(self):
        return self.expenses

class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.repo = FakeRepository()
        self.service = BudgetService(self.repo)

    def test_lisaa_kulu_tallentuu_repositoryyn(self):
        self.service.lisaa_kulu(100, "ruoka")
        kulut = self.service.hae_kaikki()
        self.assertEqual(len(kulut), 1)
        self.assertEqual(kulut[0][0], 100)
class BudgetService:
    def __init__(self, budget_repository, user_repository):
        self._repository = budget_repository
        self._user_repository = user_repository
        self._user = None

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)
        if not user or user["password"] != password:
            return False
        self._user = user
        return True

    def register(self, username, password):
        if self._user_repository.find_by_username(username):
            return False
        self._user_repository.create(username, password)
        return True

    def lisaa_kulu(self, maara, kategoria):
        if not self._user or maara <= 0:
            return False
        self._repository.create(maara, kategoria, self._user["username"])
        return True
    
    def delete_expense(self, expense_id):
        self._repository.delete(expense_id)

    def hae_kaikki(self):
        if not self._user:
            return []
        return self._repository.find_all(self._user["username"])
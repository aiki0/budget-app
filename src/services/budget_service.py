class BudgetService:
    """Käsittelee käyttäjien kirjautumisen ja kulujen hallinnan."""

    def __init__(self, budget_repository, user_repository):
        """Alustaa luokan annetuilla repositorioilla."""
        self._repository = budget_repository
        self._user_repository = user_repository
        self._user = None

    def login(self, username, password):
        """Kirjaa käyttäjän sisään, jos tunnus ja salasana täsmäävät."""
        user = self._user_repository.find_by_username(username)
        if not user or user["password"] != password:
            return False
        self._user = user
        return True

    def register(self, username, password):
        """Luo uuden käyttäjän, jos tunnusta ei ole jo olemassa."""
        if self._user_repository.find_by_username(username):
            return False
        self._user_repository.create(username, password)
        return True

    def add_expense(self, amount, category):
        """Lisää uuden kulun kirjautuneelle käyttäjälle."""
        if not self._user or amount <= 0:
            return False
        self._repository.create(amount, category, self._user["username"])
        return True

    def delete_expense(self, expense_id):
        """Poistaa tietyn kuln tietokannasta."""
        self._repository.delete(expense_id)

    def edit_expense(self, expense_id, new_amount, new_category):
        """Muokkaa olemassa olevan kulun summaa ja kategoriaa."""
        if not self._user or new_amount <= 0:
            return False
        self._repository.update(expense_id, new_amount, new_category)
        return True

    def get_all(self):
        """Hakee kaikki kirjautuneen käyttäjän kulut."""
        if not self._user:
            return []
        return self._repository.find_all(self._user["username"])

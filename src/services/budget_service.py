class BudgetService:
    def __init__(self, repository):
        self._repository = repository

    def lisaa_kulu(self, maara, kategoria):
        if maara <= 0:
            return False
        self._repository.create(maara, kategoria)
        return True

    def hae_kaikki(self):
        return self._repository.find_all()

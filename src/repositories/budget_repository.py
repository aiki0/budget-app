class BudgetRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, amount, category):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO expenses (amount, category) VALUES (?, ?)",
            (amount, category))
        self._connection.commit()

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()
        return rows
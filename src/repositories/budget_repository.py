class BudgetRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, amount, category, user_id):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO expenses (amount, category, user_id) VALUES (?, ?, ?)",
            (amount, category, user_id))
        self._connection.commit()

    def delete(self, expense_id):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        self._connection.commit()

    def update(self, expense_id, new_amount, new_category):
            cursor = self._connection.cursor()
            cursor.execute(
                "UPDATE expenses SET amount = ?, category = ? WHERE id = ?",
                (new_amount, new_category, expense_id))
            self._connection.commit()

    def find_all(self, user_id):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM expenses WHERE user_id = ?", (user_id,))
        return cursor.fetchall()

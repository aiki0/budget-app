class BudgetRepository:
    """Tietokantaoperaatioista vastaava luokka, joka käsittelee kuluja."""

    def __init__(self, connection):
        """Alustaa luokan annetulla tietokantayhteydellä."""
        self._connection = connection

    def create(self, amount, category, user_id):
        """Tallentaa uuden kulun tietokantaan."""
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO expenses (amount, category, user_id) VALUES (?, ?, ?)",
            (amount, category, user_id)
        )
        self._connection.commit()

    def delete(self, expense_id):
        """Poistaa tietyn kulun tietokannasta sen ID:n perusteella."""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        self._connection.commit()

    def update(self, expense_id, new_amount, new_category):
        """Päivittää olemassa olevan kulun tiedot tietokantaan."""
        cursor = self._connection.cursor()
        cursor.execute(
            "UPDATE expenses SET amount = ?, category = ? WHERE id = ?",
            (new_amount, new_category, expense_id)
        )
        self._connection.commit()

    def find_all(self, user_id):
        """Hakee kaikki tietyn käyttäjän tallentamat kulut."""
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM expenses WHERE user_id = ?", (user_id,))
        return cursor.fetchall()

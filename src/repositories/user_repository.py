class UserRepository:
    """Tietokantaoperaatioista vastaava luokka, joka käsittelee käyttäjätietoja."""

    def __init__(self, connection):
        """Alustaa luokan annetulla tietokantayhteydellä."""
        self._connection = connection

    def create(self, username, password):
        """Tallentaa uuden käyttäjän tietokantaan."""
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self._connection.commit()

    def find_by_username(self, username):
        """Hakee käyttjän tietokannasta käyttäjätunnuksen perusteella."""
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()
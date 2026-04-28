# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen pakkausrakenne noudattaa kolmikerrosarkkitehtuuria, ja koodi on jaettu seuraaviin osiin:

- **ui**: Käyttöliittymästä vastaava koodi
- **services**: Sovelluslogiikka (esim. `BudgetService`)
- **repositories**: Tietojen tallennuksesta vastaava koodi (`BudgetRepository`)
- **database**: Tietokantayhteyden hallinta ja alustus

## Käyttöliittymä

Käyttöliittymä sisältää tällä hetkellä kolme erillistä näkymää:
- Kirjautumis- ja rekisteröitymisnäkymä
- Päänäkymä (budjetin ja kulujen seuranta)
- Apunäkymä kulun muokkaamiselle

Käyttöliittymä on eriytetty täysin omaksi kokonaisuudekseen (`ui.py`), eikä se sisällä lainkaan sovelluslogiikkaa tai tietokantaoperaatioita. Se ainoastaan kutsuu `BudgetService` luokan metodeja ja päivittää näkymää sen palauttamien arvojen perusteella.

## Tietojen pysyväistallennus

Sovelluksen tietojen tallennuksesta vastaavat `BudgetRepository`- ja `UserRepository`-luokat, jotka noudattavat Repository-suunnittelumallia.

Tiedot tallennetaan paikalliseen SQLite-tietokantaan. Tietokannan alustuksesta vastaa `initialize_database.py` ja yhteyden muodostamisesta `database_connection.py`.

Tietokannassa on kaksi taulua:
- `users`: Tallentaa käyttäjien tunnukset ja salasanat.
- `expenses`: Tallentaa yksittäiset kulut (määrä ja kategoria) ja liittää ne käyttäjään ID:llä (`user_id`).

## Luokkakaavio

Tässä on sovelluksen keskeisimpien luokkien suhteita kuvaava luokkakaavio:

```mermaid
classDiagram
    UI ..> BudgetService
    BudgetService ..> BudgetRepository
    BudgetService ..> UserRepository
    BudgetRepository ..> Database
    UserRepository ..> Database

    class UI {
        +start_ui()
        +show_login()
        +show_main()
    }

    class BudgetService {
        -user
        +login(username, password)
        +register(username, password)
        +add_expense(amount, category)
        +delete_expense(expense_id)
        +edit_expense(expense_id, new_amount, new_category)
        +get_all()
    }

    class BudgetRepository {
        +create(amount, category, user_id)
        +delete(expense_id)
        +update(expense_id, new_amount, new_category)
        +find_all(user_id)
    }

    class UserRepository {
        +create(username, password)
        +find_by_username(username)
    }

    class Database {
        +get_database_connection()
    }
```
## Sovelluslogiikka

Tässä kuvataan sovelluksen toimintaa sekvenssikaavioiden avulla:
### Kulun lisääminen
Kun käyttäjä syöttää kulun tiedot ja klikkaa tallennuspainiketta, ohjelman sisäinen eteneminen tapahtuu seuraavasti:
```mermaid
sequenceDiagram
    actor User
    participant UI
    participant BudgetService
    participant BudgetRepository
    participant Database

    User->>UI: Syöttää tiedot ja klikkaa "Tallenna kulu"
    UI->>BudgetService: add_expense(10, "ruoka")
    BudgetService->>BudgetRepository: create(10, "ruoka", "matti")
    BudgetRepository->>Database: INSERT INTO expenses...
    Database-->>BudgetRepository: OK
    BudgetRepository-->>BudgetService: OK
    BudgetService-->>UI: True
    UI->>BudgetService: get_all()
    BudgetService-->>UI: expenses list
    UI->>User: päivittää listanäkymän
```
### Kulun muokkaaminen
Kun käyttäjä valitsee kulun, avaa muokkausikkunan, syöttää uudet tiedot ja tallentaa muutokset, ohjelma etenee seuraavasti:
```mermaid
sequenceDiagram
    actor User
    participant UI
    participant BudgetService
    participant BudgetRepository
    participant Database

    User->>UI: Syöttää uudet tiedot ja klikkaa "Tallenna muutokset"
    UI->>BudgetService: edit_expense(1, 100, "uusi kategoria")
    BudgetService->>BudgetRepository: update(1, 100, "uusi kategoria")
    BudgetRepository->>Database: UPDATE expenses SET...
    Database-->>BudgetRepository: OK
    BudgetRepository-->>BudgetService: OK
    BudgetService-->>UI: True
    UI->>BudgetService: get_all()
    BudgetService-->>UI: expenses list
    UI->>User: Sulkee apuikkunan ja päivittää listan
```
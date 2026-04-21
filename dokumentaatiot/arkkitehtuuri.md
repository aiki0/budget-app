# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen pakkausrakenne noudattaa kolmikerrosarkkitehtuuria, ja koodi on jaettu seuraaviin osiin:

- **ui**: Käyttöliittymästä vastaava koodi
- **services**: Sovelluslogiikka (esim. `BudgetService`)
- **repositories**: Tietojen tallennuksesta vastaava koodi (`BudgetRepository`)
- **database**: Tietokantayhteyden hallinta ja alustus

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
        +get_all()
    }

    class BudgetRepository {
        +create(amount, category, user_id)
        +delete(expense_id)
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
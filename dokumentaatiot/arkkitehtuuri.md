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
    BudgetRepository ..> Database

    class UI {
        +start()
    }

    class BudgetService {
        +lisaa_kulu(maara, kategoria)
        +hae_kaikki()
    }

    class BudgetRepository {
        +create(amount, category)
        +find_all()
    }

    class Database {
        +get_database_connection()
    }
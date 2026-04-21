# Changelog

## Viikko 3

- Ei mitään

## Viikko 4

- Käyttäjä voi tallentaa menoja ja tuloja pysyvästi tietokantaan
- Käyttäjä näkee ajantasaisen rahatilanteen heti muutosten jälkeen
- Lisätty `BudgetRepository`-luokka, joka vastaa tietojen tallennuksesta SQLite-tietokantaan
- Lisätty `BudgetService`-luokka, joka vastaa sovelluslogiikasta ja erottaa sen käyttöliittymästä
- Toteutettu tietokannan alustus `initialize_database.py`-tiedoston avulla
- Koodin laadun parannus kokonaisuudessaan

## Viikko 5

- Toteutettu käyttäjien rekisteröinti ja kirjautuminen
- Kulut tallennetaan ja haetaan nyt käyttäjäkohtaisesti (oma näkymä jokaiselle käyttäjälle)
- Lisätty toiminnallisuus kulujen poistamiseen tietokannasta
- Lisätty `UserRepository`-luokka käyttäjätietojen hallintaan
- Testien päivittäminen vastaamaan uutta logiikkaa
- Luokkakaavion päivitys sekä sekvenssikaavion lisäys
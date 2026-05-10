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

## Viikko 6

- Lisätty käyttäjälle mahdollisuus muokata olemassa olevien kulujen summaa ja kategoriaa
- Kirjoitettu Docstring-dokumentaatiot sovelluksen lähes kaikkialle
- Lisätty tietokantaoperaatioiden testaus käyttämällä SQlite-testitietokantaa
- Nostettu testikattavuus reilusti yli 60 % rajan

## Viikko 7

- Poistettu tietokantapolun kovakoodaus ja toteutettu sovelluksen konfigurointi `.env`-tiedoston avulla
- Lisätty `src/config.py`-tiedosto ympäristömuuttujien ja hakemistopolkujen keskitettyyn hallintaan
- Toteutettu automaattinen `data`-hakemiston luonti sovelluksen käynnistyksen yhteydessä virheiden välttämiseksi
- Parannettu virheiden käsittelyä ja validointia: kulun lisääminen tai muokkaaminen tyhjällä kategorialla estetty
- Päivitetty testit käyttämään sovelluksen oikeaa konfiguraatiota ja alustusskriptejä integraatiotesteissä
- Viimeistelty kaikki projektin dokumentit
- Luotu projektista GitHub-release "loppupalautus"
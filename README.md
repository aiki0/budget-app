# Budjetointisovellus

> Ohjelmistotekniikka-kurssin harjoitustyö.

### Dokumentaatio
-  [Vaatimusmäärittely](./dokumentaatiot/vaatimusmaarittely.md)
-  [Työaikakirjanpito](./dokumentaatiot/tyoaikakirjanpito.md)
-  [Arkkitehtuurikuvaus](./dokumentaatiot/arkkitehtuuri.md)
-  [Changelog](./dokumentaatiot/changelog.md)

### Harjoitukset (Laskarit)
- [Laskarit-hakemisto](./laskarit)
- [Viikko 1](./laskarit/viikko1.md)


## Käyttöohje

### Asennus ja alustus

Varmista ennen käyttöä, että olet asentanut Python-riippuvuudet Poetrylla:

```bash
poetry install
```

Ennen sovelluksen ensimmäistä käynnistystä suorita tarvittavat alustustoimenpiteet (kuten tietokannan luominen):

```bash
poetry run invoke build
```

### Sovelluksen käynnistäminen

Sovelluksen voi käynnistää seuraavalla komennolla:

```bash
poetry run invoke start
```

### Invoke-tehtävät

Projektissa on käytössä useita Invoke-komentoja kehityksen tueksi:

| Komento | Toiminto |
| :--- | :--- |
| `poetry run invoke build` | Alustaa tietokannan ja valmistaa sovelluksen suoritusta varten |
| `poetry run invoke start` | Käynnistää sovelluksen komentorivikäyttöliittymän |
| `poetry run invoke test` | Suorittaa automaattiset yksikkötestit |
| `poetry run invoke lint` | Suorittaa koodin laadun tarkistuksen Pylintillä |
| `poetry run invoke coverage-report` | Muodostaa testikattavuusraportin (HTML) |

HTML-muotoinen kattavuusraportti löytyy suorituksen jälkeen projektin juuren *htmlcov*-hakemistosta.

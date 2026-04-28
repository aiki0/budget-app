# Käyttöohje

Lataa sovelluksen uusin release ja suorita asennus [README.md](../README.md)-tiedoston ohjeiden mukaisesti.

## Sovelluksen käynnistäminen

Kun olet alustanut tietokannan (`poetry run invoke build`), sovellus käynnistetään komennolla:
`poetry run invoke start`

## Kirjautuminen ja rekisteröityminen

Sovelluksen käynnistyessä aukeaa kirjautumisnäkymä. 
* Jos olet uusi käyttäjä: syötä haluamasi käyttäjätunnus ja salasana ja paina "Rekisteröidy". Tämän jälkeen voit kirjautua sisään samoilla tunnuksilla.
* Jos sinulla on jo tunnus: syötä käyttäjätunnus ja salasana niille varattuihin kenttiin ja paina "Kirjaudu".


## Kulujen hallinta

Kun olet kirjautunut sisään, näet päävalikon ja listan aiemmin tallentamistasi kuluista.

### Kulun lisääminen
1. Syötä "Määrä"-kenttään haluamasi summa numeroina.
2. Syötä "Kategoria"-kenttään kulun tyyppi (esim. "ruoka" tai "bensa").
3. Paina "Tallenna kulu". Kulu ilmestyy näytöllä olevaan listaan.

### Kulun muokkaaminen
1. Valitse haluamasi kulu hiirellä klikkaamalla listasta.
2. Paina "Muokkaa valittua" -nappia.
3. Aukeavaan ikkunaan voit muuttaa summan ja kategorian.
4. Paina "Tallenna muutokset".

### Kulun poistaminen
1. Valitse poistettava kulu listasta klikkaamalla sitä.
2. Paina "Poista valittu" -nappia. Kulu poistuu listalta ja tietokannasta pysyvästi.
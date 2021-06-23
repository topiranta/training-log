# Training log

Web-applikaatio, jolla voi pitää kirjaa ja suunnitella useamman lajin harjoittelua. Helsingin yliopiston kurssin *[Tietokantasovellus](https://hy-tsoha.github.io/materiaali/pages/aikataulu.html)* laboratoriotyö.

## Sovelluksen tila ja ominaisuudet 23.6.

Tuotantosovellus kokeiltavissa [Herokussa](https://tsoha-training-log.herokuapp.com/).
Herokussa pyörivän sovelluksen tietokannassa on yksi admin-käyttäjä:
* Käyttäjätunnus poliisimestari
* Salasana sisu
Admin-tunnuksella voi muuttaa muiden käyttäjätunnusten käyttäjätasoja.

### Ominaisuudet

* Käyttäjä voi luoda käyttäjätunnuksen
  * Käyttäjätunnuksen tulee olla uniikki
  * Käyttäjää luodessa salasana tulee syöttää kaksi kertaa
  * Sovellus osaa näyttää kirjautumissivulla erilaiset virheviestit
* Käyttäjä voi kirjautua sisään
* Käyttäjä voi luoda uuden harjoituksen ja antaa sille kuvauksen, lajin, pituuden, ajan sekä keskisykkeen
* Käyttäjä näkee omat harjoituksensa
* Käyttäjä voi avata harjoituksen oman sivun
* Käyttäjä voi kirjoittaa harjoitukselle kommentin
* Käyttäjä näkee harjoituksen kommentit
* Käyttäjä voi kirjautua ulos
* Valmentaja näkee kaikkien harjoitukset
* Valmentaja voi kirjoittaa kaikkiin harjoituksiin kommentin
* Valmentaja näkee kaikki käyttäjät
* Admin näkee kaikkien harjoitukset
* Admin voi avata kaikkien harjoitusten sivut
* Admin voi kirjoittaa kaikkin harjoituksiin kommentin
* Admin näkee kaikki käyttäjät ja voi muokata näiden käyttäjänimeä sekä käyttäjätasoa

## Välipalautus 2 30.5.2021

Sovelluksesta on toimiva versio [Herokussa](https://tsoha-training-log.herokuapp.com/).

Sovellus hakee etusivulle kantaan merkityt harjoitukset ja käyttäjä voi lisätä etusivulla uusia harjoituksia.

## Välipalautus 1

Sovelluksen keskeiset toiminnallisuudet:

* Käyttäjä voi luoda suoritetun harjoituksen, johon kuuluvat:
  * Päivämäärä
  * Laji
  * Kesto
  * Pituus kilometreissä
  * Keskisyke
  * Kuvaus
* Käyttäjä voi luoda etukäteen suunniteltuja harjoituksia
* Käyttäjä voi merkitä suunnitellun harjoituksen suoritetuksi
* Käyttäjä voi lisätä kommentin harjoitukseen
* Käyttäjä näkee vain omat harjoituksensa
* Valmentaja näkee kaikkien käyttäjien harjoitukset
* Valmentaja voi kommentoida käyttäjien harjoituksia
* Valmentaja voi luoda käyttäjälle suunnitellun harjoituksen

Readme-versio 0.4

# Ohjelmistotekniikka harjoitustyö
## Skyrim Character Generator

Sovelluksen on tarkoitus olla tukena The Elder Scrolls V: Skyrim pelin pelattavuuden parantamisessa. Sovellus generoi satunnaisen pelihahmon, jonka mukaan Skyrimiä tulee pelata. Sovellus myös personoi valitulle hahmolle tässä vaiheessa yhden pää "questlinen", joka tukee luodun hahmon vahvuuksia. Tällä hetkellä käyttäjä voi generoida itsellensä satunnaisia hahmoja ja tulostaa listan generoiduista hahmoista. Käyttäjä voi myös hakea neuvoja hänen generoimilleen hahmoille.

## Huomioita
Sovellus on testattu toimivan Python 3.8.10 tai uudemmalla versiolla. Invoke puutteiden takia sovellus toimii tällä hetkellä esim. VSC kautta käyttäen suorittaen main.py tiedoston.

## Käyttöohjeet

- Asenna riippuvuudet komennolla

```bash
poetry install
```
- Käynnistä ohjelma komennolla

```bash
poetry run invoke start
```

- Käytettävissä olevat toiminnot

```bash
0: keskeyttää ohjelman suorituksen
1: generoi pelihahmon
2: tulostaa kaikki generoidut pelihahmot
```

## Muuta toiminnallisuutta

- Testien suoritus

```bash
poetry run invoke test
```
- Testikattavuusraportti

```bash
poetry run invoke coverage-report
```

- Koodin formatointi

```bash
poetry run invoke format
```

- Pylintin suoritus

```bash
poetry run invoke lint
```

### Dokumentaatio
[Työaikakirjanpito](https://github.com/sampsaol/ot-harjoitustyo/blob/7494ab5213f6d2eb892a2f86868066a86a321603/dokumentaatio/tyoaikakirjanpito.md)

[Vaatimusmäärittely](https://github.com/sampsaol/ot-harjoitustyo/blob/7494ab5213f6d2eb892a2f86868066a86a321603/dokumentaatio/vaatimusmaarittely.md)

[Changelog](https://github.com/sampsaol/ot-harjoitustyo/blob/b9cbd1449272c7199f55b92a3e5d61c5af15f5c6/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/sampsaol/ot-harjoitustyo/blob/db94bb39932c8a92c3abb49eeeaa93c7dd167012/dokumentaatio/arkkitehtuuri.md)

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
3: valitse generoiduista pelihahmoista, mille haluat tulostaa ohjeistuksen
4: poistaa kaikki tallennetut generoidut hahmot
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
[Työaikakirjanpito](https://github.com/sampsaol/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Vaatimusmäärittely](https://github.com/sampsaol/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Changelog](https://github.com/sampsaol/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/sampsaol/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Viimeisin release](https://github.com/sampsaol/ot-harjoitustyo/releases/tag/viikko5.1)

[Toimiva release](https://github.com/sampsaol/ot-harjoitustyo/releases/tag/viikko5.2)

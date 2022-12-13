# Arkkitehtuurikuvaus
## Rakenne

Ohjelma noudattaa kerrosarkkitehtuuria, missä *ui* perii osan *services* ja *generators* hakemistojen luokista ja *services* perii *generators* ja *repositories* hakemistojen luokkia.
Ohjelman pakkausrakenne on seuraavanlainen:

```mermaid
classDiagram
  ui ..> services 
  services ..> generators
  services ..> repositories
  ui ..> generators

  class ui{
  }
  class services{
    character_service
  }
  class generators{
    classes
    races
    quests
    guide
  }

```
*ui* vastaa sovelluksen käyttöliittymästä, *services* vastaa sovelluslogiikasta, *generators* vastaa hahmojen tuottamisesta ja *repositories* vastaa tietojen tallennuksesta.

```mermaid
sequenceDiagram


```

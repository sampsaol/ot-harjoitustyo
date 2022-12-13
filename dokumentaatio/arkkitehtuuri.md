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

## Päätoiminnallisuudet
```mermaid
sequenceDiagram
participant user
participant ui
participant services
participant generators
participant repositories
user->>+ui: main()
ui->>user: Command:
user->>ui: "1"
ui->>+services: generate_character()
services->>+generators: generate_character()
generators->>-services: (race, class, quest)
services->>+repositories: add_character((race,class,quest))
repositories->>-services: (race,class,quest)
services->>-ui: (race,class,quest)
ui->>-user: "Your race will be {race} and your class will be {class}. Your primary questline is {quest}

```
Käyttäjä voi generoida satunnaisia pelihahmoja itselleen, jotka sovellus sitten tallentaa määriteltyyn tiedostoon. Käyttäjä antaa UI:lle komennon, UI lähettää sen CharacterServiceen, joka generoi generators hakemiston avulla rodun, pelityylin ja questlinen. Sitten CharacterService tallentaa tiedoston repositories avulla ja lähettää generoidun hahmon UI:lle joka tulostaa sen käyttäjälle.

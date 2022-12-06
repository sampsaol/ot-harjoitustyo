```mermaid
classDiagram
  ui <.. services
  services <.. generators
  ui <.. generators

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

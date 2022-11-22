```mermaid
classDiagram
  Peli "1" ..> "2" Noppa
  Peli "1" ..> "2..8" Pelaaja
  Peli "1" -- "1" Pelilauta
  Pelaaja "1" -- "1" Pelinappula
  Pelinappula "2..8" -- "1" Peliruutu
  Pelilauta "1" -- "40" Peliruutu
  Peliruutu "1" -- "1" Seuraava peliruutu
  }
 ```

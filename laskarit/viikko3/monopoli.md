```mermaid
classDiagram
  Peli "1" ..> "2..8" Pelaaja
  Peli "1" ..> "1" Pelilauta
  Peli "1" ..> "2" Noppa
  Pelaaja "1" -- "1" Pelinappula
  Pelinappula "0..8" ..> "1" Peliruutu
  Pelilauta "1" -- "40" Peliruutu
  class Peliruutu{
    seuraava_ruutu
  }
 ```

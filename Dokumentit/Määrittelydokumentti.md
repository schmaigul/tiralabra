# Määrittelydokumentti

Projektin idea on luoda Connect Four-tekoäly jota vastaan pelaaja voi sitten pelata. Tämän lisäksi on mahdollisuus luoda eri versioita tekoälystä ja vertailla kuinka hyvin ne pärjäävät toisiaan vastaan. Projektin toteutuksessa aion käyttää Pythonia ja pygame-kirjastoa grafiikoille. Omaan tarpeeksi hyvät taidot seuraavissa ohjelmointikielissä vertaisarviointia varten:
- C++
- Java
- Javascript
- C

Algoritmeina toimii Minimax ja Alpha-beta pruning joihin tavoitteena olisi lisätä vielä heuristiikkaa jos aika sen sallii. Algoritmi luo search treen, jota pitkin kulkee DFS:llä. Alpha-beta pruning yrittää eliminoida puun oksia sille annetun pisteytyksen perusteella päätöksenteon nopeuttamiseksi. Tietorakenteina toimivat todennäköisimmin 2D-matriisit joiden avulla voidaan tallentaa pelin tiloja.

Projektin tavoittteena on selvittää mitkä arvot pelin eri tiloihin ovat optimaaliset oikeaa ihmistä vastaan, ja vertailla tuloksia antamalla algoritmin mennä puun eri syvyyksiin. Valitsin aiemmin mainitut algoritmit syystä että pääsen itse määrittelemään pelin eri tilan arvot ja hiomaan tekoälyn ilman ennakkoon annettuja optimaalisinta ratkaisua. 

Ohjelma saa syötteenä peliruudukon sarakkeen numeron johon Connect Four tapaan sijoitetaan nappula.

### Aikavaativuudet:
Minimax
- Aikavaativuus: O(b^d) missä b = solmujen määrä ja d = puun syvyys
- Tilavaativuus: O(bd)

Minimax + Alpha-beta pruning:
- Aikavaativuus: Worst case: O(b^d), Best case: O(b^(d/2))
- Tilavaativuus: O(bd)

Lähteinä esimerkiksi:

https://en.wikipedia.org/wiki/Minimax

https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

https://medium.com/analytics-vidhya/artificial-intelligence-at-play-connect-four-minimax-algorithm-explained-3b5fc32e4a4f


Opinto ohjelma: Bachelor's in science

Kieli: Suomi

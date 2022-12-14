
# Toteutus

Ohjelma koostuu päätiedostoista AIConnectfour, ConnectFour, ja utils-moduulista, jossa sijaitsee pelilogiikka.

Board_logic sisältää pelilaudan logiikan, kuten voittotilanteen tarkistuksen, uuden pelinappulan asettaminen laudalle ja pelilaudan piirtäminen graafisesti ikkunaan. 

AI_logic käyttää monia board_logic-tiedoston funktioita, muttei sekään ole luokka. Tämä metodeja täynnä oleva tiedosto sisältää tekoälyn logiikan, kuten pelitilanteen arvioinnin, minimax ja alpha beta-pruning algoritmit.

AI_logic ja Board_logic linkitetään AIConnectfour.py käyttöliittymään, joka käynnistää pelin ja luo peli-ikkunan. Tämän jälkeen peli alkaa, kunnes toinen on voittanut. Peli alkaa alusta neljän sekunnin jälkeen päättymisestä.

Alla esimerkki käyttöliittymästä

![image](../pics/AI_wins.png)

# Botin toiminta

Tekoäly käyttää alpha-beta pruning algoritmia, joka on edistyneempi versio minimax-algoritmista. Karsintaa on vielä paranneltu käyttäen iteratiivista syvenemistä, joka käytännössä tutkii hakupuun syvyyksiä kasvavilla syvyysrajoilla. 

Ohjelmassani tekoäly pyrkii maksimoivan pisteensä. Maksimointi-funktio pyrkii löytämään eniten pisteitä antavan lapsisolmun. Lapsisolmut ovat kaikki pelilaudan seuraavat mahdolliset tilat, eli kaikki paikat, minne pelinappulan voi pudottaa laudalle. Lapsisolmujen generoimisen jälkeen vaihdetaan pelivuoro vastustajalle, ja kutsutaan minimoiva funktio, joka pyrkii keräämään pienimmät pisteet näiltä uusilta lapsisolmuilta. Jos jokin lapsisolmuista johtaa voittotilanteeseen, palautetaan erittäin suuri tai pieni arvo riippuen onko maksimoivan vai minivoivan vuoro. Jos kuitenkin päädytään hakupuun pohjalle, kutsutaan pisteytysfunktio, joka arvioi solmun pelitilanteen ja palauttaa sen.

Pisteytysfunktio tarkistaa nykyisen pelaajan kuten myös vastustajan mahdollisuudet voittaa kyseisellä laudalla. Tämä perustuu funktion tarkistamaan niin sanottuja "ikkunoita" pelilaudalta. Ikkuna on neljän pituinen lista, joka on osajoukko pelilaudasta. Kaikki mahdolliset ikkunat generoidaan sen omalla funktiolla, jotka sitten annetaan pisteytysfunktiolle. Pisteitä annetaan, jos ikkunassa esiintyy vain omia pelinappuloita. Mitä enemmän omia pelinappuloita ikkunassa esiintyy, sitä enemmän pisteitä jaetaan. Pisteytysfunktio tarkistaa myös vastustajan pisteet, ja vähentää ne loppupisteytyksestä. 

Lisäheuristiikkana toimii iteratiivinen syventäminen, jonka avulla alpha-beta karsintaa saadaan optimoitua järjestämällä lapsisolmujen pisteet parhaimmasta huonoimpaan joka silmukan jälkeen. Syvenenimen siis alkaa nollasta ja menee johonkin tiettyyn syvyyteen. 

## Aikavaativuudet

Iteratiivinien syveneminen aloittaa syvyydestä 0 ja nostaa syvyyttä johonkin syvyyteen d. Joka syvyydessä käydään maksimissaan b solmua läpi. Jos alpha-beta ei mitään, aikavaativuus on (d)b + (d-1)b^2 + ... + (2)b^d-1 + b^d = O(b^d). Parhaassa tilanteessa alpha-beta pruning onnistuu karsimaan aina toisen vuorolla kaikki muut paitsi yhden solmun silloin kun solmujen järjestys on hyvä. Tällöin paras mahdollinen aikavaativuus on O(b^(d/2)), joka saattaa olla lähempänä totuutta. Koodissa on käytetty pieniä kikkoja, kuten lapsisolmujen generoimisen järjestyksen parantamista ja juuren aloittavan aina etsmisien aina aikaisemman etsinnän parhaasta vaihtoehdosta.

## Tilavaativuudet

Joka tasolla talletetaan yksi arvo jokaista laillista lapsisolmua kohtaan, joten tasolla d tilavaativuus on O(bd), jossa b on lapsisolmujen määrä. Muuta ei algoritmin itse tarvitse tallentaa.

## Puutteet ja parannusehdotukset

Projektia olisi mahdollista parantaa vaikka kuinka monella tavalla, kuten välimuistilla ja alpha-beta ikkunoiden optimoimisella. Halusin oikeastaan toteuttaa nämä kaikki ominaisuudet, mutta se olisi ollut itselleni liian haastavaa ja olisi vienyt liikaa aikaa. Pisteytysmetodia voisi muuttaa paremmaksi, painottaen myöskin syvyyttä pisteiden arvioimisessa. Mitä syvemmälle pelipuu on mennyt, sitä epätodennäköisempää on sen esiintyä pelin aikana. Pienet syvyydet voisivat antaa enemmän pisteitä iteratiivisessa syvenemisessä, jolloin karsintaakin koituisi enemmän, ja tekoöäly painottaisi nopeaa ja varmaa voittoa. Välimuistia voisi käyttää aikaisempien pelitilojen arvojen tallettamiseen, jolloin tulevat pelitilat olisi helppo tarkistaa muistista, ja mahdollisesti palauttaa välittömästi jokin arvo. 

# Lähteet:

https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search

https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

https://medium.com/analytics-vidhya/artificial-intelligence-at-play-connect-four-minimax-algorithm-explained-3b5fc32e4a4f




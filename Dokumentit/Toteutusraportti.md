
Ohjelma koostuu päätiedostoista AIConnectfour, ConnectFour, ja utils-moduulista, jossa sijaitsee pelilogiikka.

Board_logic sisältää pelilaudan logiikan, kuten voittotilanteen tarkistuksen, uuden pelinappulan asettaminen laudalle ja pelilaudan piirtäminen graafisesti ikkunaan. 

AI_logic käyttää monia board_logic tiedoston funktioita, muttei sekään ole luokka. Tämä metodeja täynnä oleva tiedosto sisältää tekoälyn logiikan, kuten pelitilanteen arvioinnin, minimax ja alpha beta-pruning algoritmit.

AI_logic ja Board_logic linkitetään AIConnectfour.py käyttöliittymään, joka käynnistää pelin ja luo peli-ikkunan. Tämän jälkeen peli alkaa, kunnes toinen on voittanut. Peli alkaa alusta neljän sekunnin jälkeen päättymisestä.

## Aikavaativuudet

Iteratiivinien syveneminen aloittaa syvyydestä 0 ja nostaa syvyyttä johonkin syvyyteen d. Joka syvyydessä käydään maksimissaan b solmua läpi. Jos alpha-beta ei mitään, aikavaativuus on (d)b + (d-1)b^2 + ... + (2)b^d-1 + b^d = O(b^d). Parhaassa tilanteessa alpha-beta pruning onnistuu karsimaan aina toisen vuorolla kaikki muut paitsi yhden solmun silloin kun solmujen järjestys on hyvä. Tällöin paras mahdollinen aikavaativuus on O(b^(d/2)), joka saattaa olla lähempänä totuutta. Koodissa on käytetty pieniä kikkoja, kuten lapsisolmujen generoimisen järjestyksen parantamista ja juuren aloittavan aina etsmisien aina aikaisemman etsinnän parhaasta vaihtoehdosta.

## Tilavaativuudet

Joka tasolla talletetaan yksi arvo jokaista laillista lapsisolmua kohtaan, joten tasolla d tilavaativuus on O(bd), jossa b on lapsisolmujen määrä. Muuta ei algoritmin itse tarvitse tallentaa.

## Puutteet ja parannusehdotukset

Projektia olisi mahdollista parantaa vaikka kuinka monella tavalla, kuten välimuistilla ja alpha-beta ikkunoiden optimoimisella. Halusin oikeastaan toteuttaa nämä kaikki ominaisuudet, mutta se olisi ollut itselleni liian haastavaa ja olisi vienyt liikaa aikaa. Pisteytysmetodia voisi muuttaa paremmaksi, painottaen myöskin syvyyttä pisteiden arvioimisessa. Mitä syvemmälle pelipuu on mennyt, sitä epätodennäköisempää on sen esiintyä pelin aikana. Pienet syvyydet voisivat antaa enemmän pisteitä iteratiivisessa syvenemisessä, jolloin karsintaakin koituisi enemmän, ja tekoöäly painottaisi nopeaa ja varmaa voittoa. Välimuistia voisi käyttää aikaisempien pelitilojen arvojen tallettamiseen, jolloin tulevat pelitilat olisi helppo tarkistaa muistista, ja mahdollisesti palauttaa välittömästi jokin arvo. 
Vaadittavat kirjastot: Pygame ja Numpy

## Ohjelma aloitetaan suorittamalla AIConnectFour.py komennolla
python AIConnectFour

Ohjelma koostuu päätiedostosta AIConnectfour, ja aputiedostoista ai_logic ja board_logic

Board_logic sisältää pelilaudan logiikan, kuten voittotilanteen tarkistuksen, uuden pelinappulan asettaminen laudalle ja pelilaudan piirtäminen graafisesti ikkunaan

AI_logic käyttää monia board_logic tiedoston funktioita, muttei sekään ole luokka. Tämä tiedosto sisältää tekoälyn logiikan, kuten pelitilanteen arvioinnin, minimax ja alpha beta-pruning algoritmit.

Oletuksena ihmispelaaja aloittaa pelin.

## Miten pelata

Suorita komento **python AIConnectFour**, niin peli-ikkuna aukeaa. Tämän jälkeen peli ilmoittaa, kumman vuoro on aloittaa. Kun peli sanoo, 'human's turn', on sinun vuoro valita hiirellä haluamasi sarake, minne pelinappula putoaa. Tämän jälkeen tekoäly valitsee siirtonsa, kunnes on taas sinun vuoro valita. Peli etenee kunnes jompi kumpi voittaa. Peli alkaa alusta 4-sekunnin kuluttua.
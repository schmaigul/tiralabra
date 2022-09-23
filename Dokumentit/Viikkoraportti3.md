Aloitin viikon luomalla uuden luokan tekoälyä varten. AIConnectFour-luokka perii ConnectFour-luokan metodit, ja lisää logiikan pelitilan arvioimiseen ja alpha-beta pruning funktionaalisuuden. Loin ensiksi make_children()-metodin, joka generoi kaikki sen hetkisen pelaajan lailliset siirrot, ja luo niistä listan AIConnectFour-luokkia. Tämä vie reilusti enemmän muistia kuin vain uusien matriisien luominen, mutta tekee muiden metodien toteuttamisen helpommaksi, kun kaikki aikaisemmat metodit ovat käytössä lapsisolmuillekkin.

Jatkoin projektia ensin tekemällä yksinkertaisen minimax-algoritmin, ja logiikan pelitilan arvojen laskemiseen. Tämä vei eniten aikaa, sillä olin liian ahne alussa ja loin liian monimutkaisen logiikan jota en itse ymmärtänyt. Lyhyen googlailun jälkeen huomasin kuinka muut algoritmit käyttivät ideaa, jossa arviointifunktio arvioi pelilaudan kaikkia osajoukkoja yhteisellä funktiolla. Tämä osoittaitui tehokkaaksi, ja nyt tekoäly on jo tarpeeksi viisas voittamaan keskiverto pelaajan. Lopuksi lisäsin alpha-beta karsinnan, joka oli nopeaa ja toimi ensimmäisellä testillä. 

Tekoäly pelaa erittäin puolustavalla tavalla, yrittäen estää vastustajan voiton. 

Tämän jälkeen aloitin yksikköstestauksen luomisen, johon lisäsin voittotilanteen tarkistamisen testauksen ja muita pelilogiikan olennaisimpien funktioiden testejä. 

Projekti on edennyt jo todella pitkälle. Tekoälyä voi hioa aina pidemmälle, mutta se saattaa olla haastavaa. Alan ensi viikolla testaamaan algoritmin nopeutta eri pelipuun syvyyksillä, ja pyrin luomaan algoritmia hieman nopeammaksi ja siistin koodia.

Aikaa tälllä viikolla meni noin 20h
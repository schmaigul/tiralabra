Kirjoitin tällä viikolla koko projektin uudestaan, siksi, koska luokkaolioiden käyttö osoittaitui erittäin hitaaksi. Loin kaikki aikaisemmat funktiot ja metodit, mutta tällä kertaa en tallentanut jokaista pelitilannetta omaan luokkaansa, vain pelkästään 2D-matriiseihin. Koodin kirjoituksen jälkeen AI oli noin 5-kertaa nopeampi. Yksi tärkeimmistä muutoksista oli lapsisolmujen generoimisessa, jossa ennen loin jokaista solmua kohden uuden luokan. Nyt palautin ainoastaan listan kaikista valideista sarakkeista, johon pelinappulan pystyy putoamaan. Lapsien generointi alkaa nyt myös laudan keskeltä liikkuen kumpaankin suuntaan. Tämä on optimaalisempi tapa kuin aloittaa jommasta kummasta sivusta edeten toiseen reunaan. 

Koodin uudelleenkirjoittamisen jälkeen yritin ymmärtää syventävää iterointia, joka on aika suuri määrä lisätyötä nykyiseen koodipohjaan. Tarkoitus olisi saada tämä jollain tavalla toimimaan, mutta pelkästään algoritmin ymmärtäminen ja lähteiden löytäminen vei erityisen paljon aikaa. Syventävä iterointi vaatisi transpoosipöydän ja alpha-beta ikkunoiden kanssa leikkimistä, jonka avulla aikaisempia siirtoja voidaan käyttää hyväksi tulevien pelitilanteiden arvoimiseen. Saatan ensi viikolla ainakin yrittää toteuttaa tätä, vaikka olen jo kyllin tyytyväinen nykyisen botin performanssiin. 

Haluaisin tietää, onko joku tällä kurssilla toteuttanut syventävää iterointia? Nimittäin sen vaativuus kurssiin nähden on aika suuri.

Olen myös testaillut bottia antaen ystävieni pelata sitä vastaan. Botti voittaa noin 9/10 ottelua. Nämä voitot tapahtuvat aina vasta pelin lopussa, kun vapaita paikkoja on jäljellä vain muutamia. Tämä ilmiö johtuu siitä, että botti ei pysty ennakoimaan niin pitkälle tulevaisuuteen, kunnes on jo liian myöhäistä.

En kerennyt luoda enempää testejä ennen palautusta, mutta ensi viikolla hoidan nuo kaikki dokumentoinnnit pois alta ennen kuin yritän parantaa botin suorituskykyä.

Aikaa käytetty tällä viikolla noin 15h
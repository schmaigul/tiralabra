### Viikkoraportti 2

Aloitin viikon tutkimalla connect four-pelin logiikkaa ja katsomalla eri lähteitä pelin toteuttamiseksi. Päätavoitteena oli saada ydinpeli toimimaan kahden ihmisen pelattavaksi, jossa onnistuin. Tämä tosin vei paljon enemmän aikaa kuin odotin, sillä edes yksinkertaisen pelin luominen oli uutta ja vierasta. Projekti alkoi luomalla tyhjä 2D-matriisi joka täyttyi nollista. Seuraavksi loin pelisilmukan, joka vaihtelee kahden pelaajan välillä. Connect four logiikan luomisessa meni parisen tuntia, eniten käytin aikaa voittoehdon tarkastamiselle, jossa ilmeni huolimattomuusongelmia. Tämän jälkeen peliä pystyi pelaamaan kahden ihmisen voimin terminaalista. Seuraavaksi vuorossa on graafinen käyttöliittymä. Tässä vaiheessa siirsin pelin laudan logiikan omaan luokkaansa.

Pygame oli mukava ottaa käyttöön. Pelin grafiikka on yksinkertainen 2D-ruudukko joka emuloi alkuperäistä 2D-matriisia johon pelin tila on tallennnettu. Pelaaja voi määrätä seuraavan nappulansa paikan hiirellä valitsemalla haluamansa sarakkeen ruudukosta. Grafiikka kertoo aina kumman vuoro on asettaa pelinappula. Jomman kumman voittaessa tai tasapelitilanteessa peli ilmoittaa erän loppuneen ja tyhjentää laudan aloittaen heti uuden erän. 

Pelin luomisessa meni sen verran aikaa etten kerenny luomaan yksikkötestausta, vaikka testailin luokan toimintaa ihan käsin. Kävin kuitenkin läpi kuinka yksikkötestaus toimii, ja toteutan testit ensi palautukseen mennessä. 

Pelin kannalta seuraava askel on luoda toimiva minimax-algoritmi ja lisätä siihen alpha-beta pruning. Pelitilanteen arvon märittelemiseen tulee menemään aikaa.

Aikaa käytetty tällä viikolla noin 10h
### Testaa toimivuus juuressa komennolla:
 python -m unittest -v test.test_minimax


## Testiraportti:

Yksikkötestauksessa testasin pelilogiikan toimivuuden ja kaikki edge-caset. Normaalit pelin funktiot kuten laillisten pelipaikkojen määrittelemisen, pelinappulan pudottaminen, ja voittotilanteen tunnistaminen käytiin täsmällisesti läpi. Sen lisäksi testasin minimax-algoritmin oikeutta, ja tein testejä eri pelitilanteen määrittelemiseksi. Testaaminen onnistuu myös ihan peliä pelaamalla. Kaikki olennaiset metodit ja funktiot joille testien tekeminen on järkevää on testattu. Testejä itseään pääsee tarkistamaan test/test_minimax.py ohjelman koodista.

```
test_ai (test.test_minimax.MinimaxTest) ... ok
test_change_turn (test.test_minimax.MinimaxTest) ... ok
test_children (test.test_minimax.MinimaxTest) ... ok
test_detect_losing (test.test_minimax.MinimaxTest) ... ok
test_detect_winning (test.test_minimax.MinimaxTest) ... ok
test_draw (test.test_minimax.MinimaxTest) ... ok
test_evaluation (test.test_minimax.MinimaxTest) ... ok
test_score (test.test_minimax.MinimaxTest) ... ok
test_winning (test.test_minimax.MinimaxTest) ... ok

----------------------------------------------------------------------
Ran 9 tests in 5.994s
OK
```

Testit kattavat kaikki metodit ja funktiot jotka vaativat testausta

![image](../pics/CoverageReport.png)

## Tekoäly vs Tekoäly testi

Testasin kuinka hyvin tekoälyt pelaavat toisiaan vastaan. Laitoin tekoälyt pelaamaan toisiaan vastaan 100 kertaa samoilla parametreillä. Noin 70% ajasta se joka aloitti ensimmäisenä voitti. Loput 30% peleistä päättyivät toisen voittoon. Yhtäkään tasapeliä ei tullut. Tämä on selitettävissä lapsisolmujen pienestä variaatiosta. Lapsisolmuja luodessa funktio valitsee 50% todennäköisyydellä, mihin suuntaan keskisarakkeesta se luo seuraavan solmun. Tämä luo pienen variaation joka peliin, kun tekoäly ei tee aina tasan samoja valintoja. Eli algoritmissa on joitain tiettyjä lapsisolmujen järjestyksen pohjalta koituvia ketjuja jotka johtavatkin ei-aloittavan voittoon. Oletuksena siis on, että ensimmäinen pelaaja voittaisi.

![image](../pics/winning_rates_aivsai.png)

### Suorita alla oleva kaavio komennolla:
python -m test.performancetesting

## Suorituskykytestit kolmelle eri pelitilanteelle

Alla olevassa kaaviossa näkyy miten nopeasti minimax alpha-beta pruning-algoritmi toimii eri pelitilanteissa. Kuten huomataan, tyhjän pelilaudan ja häviämistilanteen arvioimisessa menee erittäin kauan, vaikka haluaisimme häviämistilanteen tunnistettavan välittömästi. Tämä johtuu algoritmin luonteesta. Sen hetkinen pelaaja pyrkii aina maksimoimaan/minimoimaan pisteensä riippuen kumpi pelaaja on pelaamassa. Samalla toinen pelaaja pyrkii vastakkaisesti minimoimaan/maksimoimaan pisteensä puun alemmalla tasolla. Vaikka häviön välttävä siirto löydettäisiin heti ensimmäisenä, ei algoritmi tunnista tätä parhaaksi vaihtoehdoksi koska se ei lähes ikinä anna hyviä pisteitä. Tästä syystä algoritmi käy lähes kaikki tasot läpi etsien parempaa tulosta kunnes, päätyy valitsemaan huonon pisteiden minimoivan siirron; häviön välttämisen. Pruningia tapahtuu joka tapauksessa etenkin suuremmissa syvyyksissä, kun peli on edennyt pidemmälle ja voittotilanteet ovat havaittu.

![image](../pics/MinimaxPerformanceTest.png)

Kuvasta huomataan, että alpha-beta pruning toimii erinomaisesti voittotilanteessa, jolloin kaikilla valitsemilla syvyyksillä menee sama aika, joka on lähes välitön. Kaavion muut käyrät demonstroivat hyvin exponentiaalista kasvua syvyyden noustessa, niinkuin pitääkin.
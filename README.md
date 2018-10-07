# Analiza Votului de la Referendum
Rezultatele au fost optinute pe baza fisierelor descarcate de la adresa [prezenta.bec.ro/referendum](prezenta.bec.ro/referendum), care se gasesc si in acest repository. Exista 8 fisiere, cate 4 din cele doua zile, la orele 10, 13, 16 si 19. Fiecare fisier contine un tabel cu campurile: 
- Judet
- UAT
- Localitate
- Siruta
- Nr sectie de votare
- Nume sectie de votare
- Mediu ('U'/'R' pentru Urban/Rural)
- Votanti lista (Alegatori inscrisi pe liste permanente)
- LP (Votanti pe liste permanente)
- LS (Votanti pe liste suplimentare)
- UM (Votanti cu urna mobile)
- LT (Total votanti)


## Prezenta la vot per judet (alfabetic)
![](https://github.com/paubric/python-referendum-analysis/blob/master/Prezenta_alfabetic.png)
## Prezenta la vot per judet (crescator)
![](https://github.com/paubric/python-referendum-analysis/blob/master/Prezenta_crescator.png)
## Distributia prezentei la vot per judet
![](https://github.com/paubric/python-referendum-analysis/blob/master/Prezenta_distributie.png)
## Cea mai mare prezenta la vot (Judet/UAT/Localitate/Nume)
Masuratoare realizata prin raportul `numar total votanti impartit la numarul de alegatori inscrisi pe liste permanente`
## Cea mai mica prezenta la vot (Judet/UAT/Localitate/Nume)
Masuratoare realizata prin raportul `numar total votanti impartit la numarul de alegatori inscrisi pe liste permanente`
## Proportia de vot de pe altceva decat liste permanente per judet (alfabetic)
![](https://github.com/paubric/python-referendum-analysis/blob/master/Suplimentare_alfabetic.png)
## Proportia de vot de pe altceva decat liste permanente per judet (crescator)
![](https://github.com/paubric/python-referendum-analysis/blob/master/Suplimentare_crescator.png)
## Cel mai mare procentaj de voturi din alte surse decat listele permanente (Judet/UAT/Localitate/Nume)
Masuratoare realizata prin scaderea din 100% a raportului `numar votanti pe liste permanente impartit la numar total votanti`
## Histograma numarului de alegatori inscrisi pe sectie in functie de mediu
![](https://github.com/paubric/python-referendum-analysis/blob/master/Inscrisi_mediu.png)
## Histograma prezentei la vot pe sectie in functie de mediu
![](https://github.com/paubric/python-referendum-analysis/blob/master/Prezenta_mediu.png)

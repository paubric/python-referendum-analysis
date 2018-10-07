# Analiza Votului de la Referendum
Rezultatele au fost optinute pe baza fisierelor descarcate de la adresa [prezenta.bec.ro/referendum](prezenta.bec.ro/referendum), care se gasesc si in acest repository. Exista 10 fisiere, cate 5 din cele doua zile, la orele 10, 13, 16, 19 si 21. Fiecare fisier contine un tabel cu campurile: 
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
```
NT VÎNĂTORI-NEAMŢ VÎNĂTORI-NEAMŢ MANASTIREA SIHASTRIA 450.9 din care de pe liste permanente: 16.33
BH SÎNMARTIN BĂILE FELIX GRADINITA BAILE FELIX 224.59 din care de pe liste permanente: 13.16
AB RÎMEŢ VALEA MĂNĂSTIRII FOSTA ŞCOALĂCU CLASELE I-IV VALEA MĂNĂSTIRII 165.22 din care de pe liste permanente: 31.14
SJ DRAGU UGRUŢIU CĂMINUL CULTURAL, NR.20 163.16 din care de pe liste permanente: 3.23
GR IZVOARELE PETRU RAREŞ ŞCOALA GENERALĂ PETRU RAREŞ 161.33 din care de pe liste permanente: 38.02
SJ HIDA MILUANI CĂMINULCULTURAL 157.14 din care de pe liste permanente: 15.15
SB MUNICIPIUL SIBIU PĂLTINIŞ PĂLTINIŞ 146.15 din care de pe liste permanente: 7.89
CJ JICHIŞU DE JOS ŞIGĂU ŞCOALA GENERALĂ 142.86 din care de pe liste permanente: 26.67
TM BARA DOBREŞTI CLĂDIREA COMUNEI BARA ( FOSTASCOALĂ DOBRESTI) 139.39 din care de pe liste permanente: 39.13
CJ BOBÎLNA PRUNI CAMINUL CULTURAL PRUNI 132.0 din care de pe liste permanente: 24.24
```
## Cea mai mica prezenta la vot (Judet/UAT/Localitate/Nume)
Masuratoare realizata prin raportul `numar total votanti impartit la numarul de alegatori inscrisi pe liste permanente`
```
B MUNICIPIUL BUCUREŞTI BUCUREŞTI SECTORUL 3 COLEGIUL NAȚIONAL "MATEI BASARAB" 0.16 din care de pe liste permanente: 0.0
VS MUNICIPIUL VASLUI VASLUI ȘCOALA GIMNAZIALĂ ”CONSTANTIN PARFENE” 0.18 din care de pe liste permanente: 16.67
B MUNICIPIUL BUCUREŞTI BUCUREŞTI SECTORUL 3 ŞCOALA GIMNAZIALĂ NR.78; 0.18 din care de pe liste permanente: 25.0
B MUNICIPIUL BUCUREŞTI BUCUREŞTI SECTORUL 3 ŞCOALA GIMNAZIALĂ NR.78; 0.23 din care de pe liste permanente: 60.0
B MUNICIPIUL BUCUREŞTI BUCUREŞTI SECTORUL 3 ŞCOALA GIMNAZIALĂ NR.47; 0.27 din care de pe liste permanente: 14.29
B MUNICIPIUL BUCUREŞTI BUCUREŞTI SECTORUL 3 ŞCOALA GIMNAZIALĂ NR.55; 0.44 din care de pe liste permanente: 80.0
B MUNICIPIUL BUCUREŞTI BUCUREŞTI SECTORUL 3 ŞCOALA GIMNAZIALĂ "BARBU DELAVRANCEA" 0.46 din care de pe liste permanente: 54.55
B MUNICIPIUL BUCUREŞTI BUCUREŞTI SECTORUL 3 ŞCOALA GIMNAZIALĂ NR.55; 0.5 din care de pe liste permanente: 71.43
IS MUNICIPIUL IAŞI IAŞI ŞCOALAGIMNAZIALĂ "GHEORGHE I. BRĂTIANU" 0.54 din care de pe liste permanente: 21.43
B MUNICIPIUL BUCUREŞTI BUCUREŞTI SECTORUL 3 ŞCOALA GIMNAZIALĂ NR.55; 0.6 din care de pe liste permanente: 63.64
```
## Proportia de vot de pe altceva decat liste permanente per judet (alfabetic)
![](https://github.com/paubric/python-referendum-analysis/blob/master/Suplimentare_alfabetic.png)
## Proportia de vot de pe altceva decat liste permanente per judet (crescator)
![](https://github.com/paubric/python-referendum-analysis/blob/master/Suplimentare_crescator.png)
## Cel mai mare procentaj de voturi din alte surse decat listele permanente (Judet/UAT/Localitate/Nume)
Masuratoare realizata prin scaderea din 100% a raportului `numar votanti pe liste permanente impartit la numar total votanti`
```
B MUNICIPIUL BUCUREŞTI BUCUREŞTI SECTORUL 3 COLEGIUL NAŢIONAL "MATEI BASARAB"; 1.65 din care de pe altceva decat liste permanente: 100.0
B MUNICIPIUL BUCUREŞTI BUCUREŞTI SECTORUL 3 COLEGIUL NAȚIONAL "MATEI BASARAB" 0.16 din care de pe altceva decat liste permanente: 100.0
GL MUNICIPIUL GALAŢI GALAŢI ȘCOALA GIMNAZIALĂ NR. 20 (ȘCOALA GENERALĂ NR. 20 ”TRAIAN”) 1.69 din care de pe altceva decat liste permanente: 100.0
HR SUSENI LIBAN ŞCOALA PRIMARĂ LIBAN 12.5 din care de pe altceva decat liste permanente: 100.0
IS MOŞNA MOŞNA ȘCOALA GIMNAZIALĂ MOȘNA 1.11 din care de pe altceva decat liste permanente: 100.0
SJ DRAGU UGRUŢIU CĂMINUL CULTURAL, NR.20 163.16 din care de pe altceva decat liste permanente: 96.77
CJ MUNICIPIUL CLUJ-NAPOCA CLUJ-NAPOCA COLEGIUL ECONOMIC “IULIAN POP” 23.2 din care de pe altceva decat liste permanente: 96.76
SB MUNICIPIUL SIBIU PĂLTINIŞ PĂLTINIŞ 146.15 din care de pe altceva decat liste permanente: 92.11
HR MĂRTINIŞ COMĂNEŞTI ȘCOALA PRIMARĂ COMĂNEȘTI 4.52 din care de pe altceva decat liste permanente: 87.5
TL MURIGHIOL DUNAVĂŢU DE SUS ŞCOALA CU CLASELE I-IV DUNAVĂȚU DE SUS 19.67 din care de pe altceva decat liste permanente: 87.5
```
## Histograma procentului de vot de pe altceva decat liste permanente
![](https://github.com/paubric/python-referendum-analysis/blob/master/Suplimentare_distributie.png)
## Histograma numarului de alegatori inscrisi pe sectie in functie de mediu
![](https://github.com/paubric/python-referendum-analysis/blob/master/Inscrisi_mediu.png)
## Histograma prezentei la vot pe sectie in functie de mediu
![](https://github.com/paubric/python-referendum-analysis/blob/master/Prezenta_mediu.png)

# Utilizare 
- Instaleaza [Python](https://realpython.com/installing-python/)
- Cloneaza acest repository
- In interiorul clonei executa `python main.py`

# Contribuie / TODO
- Verifica corectitudinea rezultatelor
- Verifica corectitudinea limbajului (legaleza)
- Diacritice
- Analiza metricilor *intre* cele 10 fisiere
- Intreaba-te cand o sa mai scrii un README in romana

# Disclaimer
Nu raspund de utilizarea/interpretarea informatiilor rezultate din utilizarea programului.


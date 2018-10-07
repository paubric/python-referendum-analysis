import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import warnings
warnings.filterwarnings("ignore")

sectii = []
with open('presence_RO_2018-10-07_16-00.csv') as csvfile:
    records = csv.DictReader(csvfile)
    for sectie in records:
         sectii.append(sectie)

print('[*] Numar sectii de vot: ', len(sectii))

nume_judete = np.unique([sectii[i]['Judet'] for i in range(len(sectii))])
print('[*] Numar de judete: ', len(nume_judete)) # Sanity check
date_judete = dict((judet, np.zeros((9))) for judet in nume_judete)

for sectie in sectii:
    date_judete[sectie['Judet']][0] += int(sectie['Votanti lista'])
    date_judete[sectie['Judet']][1] += int(sectie['LP'])
    date_judete[sectie['Judet']][2] += int(sectie['LS'])
    date_judete[sectie['Judet']][3] += int(sectie['UM'])
    date_judete[sectie['Judet']][4] += int(sectie['LT'])

for judet in list(date_judete.keys()):
    date_judete[judet][5] = date_judete[judet][1] / date_judete[judet][4] # Proportie vot de pe liste permanente
    date_judete[judet][6] = date_judete[judet][2] / date_judete[judet][4] # Proportie vot de pe liste suplimentare
    date_judete[judet][7] = date_judete[judet][3] / date_judete[judet][4] # Proportie vot cu urna mobila
    date_judete[judet][8] = date_judete[judet][4] / date_judete[judet][0] # Proportie vot

mat_judete = [[judet, date_judete[judet][5], date_judete[judet][6], date_judete[judet][7], date_judete[judet][8]] for judet in list(date_judete.keys())]

# Prezenta la vot per judet (alfabetic)
plt.figure(figsize=(16, 9))
plt.title('Prezenta la vot per judet (alfabetic)')
plt.bar([mat_judete[i][0] for i in range(len(mat_judete))], [mat_judete[i][4]*100 for i in range(len(mat_judete))])
plt.savefig('Prezenta_alfabetic.png')
print('[*] Creat fisier Prezenta_alfabetic.png')
plt.clf()

# Prezenta la vot per judet (crescator)
mat_judete_temp = sorted(mat_judete, key=lambda k: k[4])
plt.title('Prezenta la vot per judet (crescator)')
plt.bar([mat_judete_temp[i][0] for i in range(len(mat_judete_temp))], [mat_judete_temp[i][4]*100 for i in range(len(mat_judete_temp))])
plt.savefig('Prezenta_crescator.png')
print('[*] Creat fisier Prezenta_crescator.png')
plt.clf()

# Distributia prezentei la vot per judet
plt.hist([mat_judete[i][4]*100 for i in range(len(mat_judete))], density=True, bins=30)
mu, std = norm.fit([mat_judete[i][4]*100 for i in range(len(mat_judete))])
plt.title('Distributia prezentei la vot per judet')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.axes().get_yaxis().set_visible(False)
plt.plot(x, p, 'k')
plt.savefig('Prezenta_distributie.png')
print('[*] Creat fisier Prezenta_distributie.png')
plt.clf()

# Proportia de vot nu de pe liste permanente per judet (alfabetic)
plt.title('Proportia de vot de pe altceva decat liste permanente per judet (alfabetic)')
plt.bar([mat_judete[i][0] for i in range(len(mat_judete))], [(1-mat_judete_temp[i][1])*100 for i in range(len(mat_judete))])
plt.savefig('Suplimentare_alfabetic.png')
print('[*] Creat fisier Suplimentare_alfabetic.png')

plt.clf()

# Proportia de vot nu de pe liste permanente per judet (crescator)
mat_judete_temp = sorted(mat_judete, key=lambda k: -k[1])
plt.title('Proportia de vot de pe altceva decat liste permanente per judet (crescator)')
plt.bar([mat_judete_temp[i][0] for i in range(len(mat_judete_temp))], [(1-mat_judete_temp[i][1])*100 for i in range(len(mat_judete_temp))])
plt.savefig('Suplimentare_crescator.png')
print('[*] Creat fisier Suplimentare_crescator.png')
plt.clf()

# Histograma numarului de alegatori inscrisi pe sectie in functie de mediu
plt.title('Histograma numarului de alegatori inscrisi pe sectie in functie de mediu')
sectii_u = [i for i, x in enumerate(range(len(sectii))) if sectii[x]['Mediu'] == 'U']
sectii_r = [i for i, x in enumerate(range(len(sectii))) if sectii[x]['Mediu'] == 'R']
plt.hist([int(sectii[j]['Votanti lista']) for j in sectii_u], bins = 100,  label='Urban')
plt.hist([int(sectii[j]['Votanti lista']) for j in sectii_r], bins = 100,  label='Rural')
plt.legend(loc='upper right')
plt.savefig('Inscrisi_mediu.png')
print('[*] Creat fisier Inscrisi_mediu.png')
plt.clf()

# Histograma prezentei la vot pe sectie in functie de mediu
plt.title('Histograma prezentei la vot pe sectie in functie de mediu')
plt.hist([int(sectii[j]['LT'])/int(sectii[j]['Votanti lista']) for j in sectii_r], bins = 100,  label='Rural')
plt.hist([int(sectii[j]['LT'])/int(sectii[j]['Votanti lista']) for j in sectii_u], bins = 100,  label='Urban')
plt.legend(loc='upper right')
plt.savefig('Prezenta_mediu.png')
print('[*] Creat fisier Prezenta_mediu.png\n')
plt.clf()

# Top sectii dupa prezenta la vot
print('[*] Cea mai mare prezenta la vot')
top = [(sectie['Judet'], sectie['UAT'], sectie['Localitate'], sectie['Nume sectie de votare'], int(sectie['LT'])/int(sectie['Votanti lista']), int(sectie['LP'])/int(sectie['LT'])) for sectie in sorted(sectii, key=lambda x: -int(x['LT'])/int(x['Votanti lista']))][:10]
for i in range(len(top)):
    print(top[i][0],top[i][1],top[i][2],top[i][3],round(float(top[i][4])*100, 2),'din care de pe liste permanente:',round(float(top[i][5])*100, 2))

# Top sectii dupa prezenta la vot
print('\n[*] Cea mai mica prezenta la vot')
top = [(sectie['Judet'], sectie['UAT'], sectie['Localitate'], sectie['Nume sectie de votare'], int(sectie['LT'])/int(sectie['Votanti lista']), int(sectie['LP'])/int(sectie['LT'])) for sectie in sorted(sectii, key=lambda x: int(x['LT'])/int(x['Votanti lista']))][:10]
for i in range(len(top)):
    print(top[i][0],top[i][1],top[i][2],top[i][3],round(float(top[i][4])*100, 2),'din care de pe liste permanente:',round(float(top[i][5])*100, 2))

# Top sectii dupa procentul voturilor din alte surse decat listele permanente
print('\n[*] Top sectii dupa procentul voturilor din alte surse decat listele permanente')
top = [(sectie['Judet'], sectie['UAT'], sectie['Localitate'], sectie['Nume sectie de votare'], int(sectie['LT'])/int(sectie['Votanti lista']), 1-(int(sectie['LP'])/int(sectie['LT']))) for sectie in sorted(sectii, key=lambda x: int(x['LP'])/int(x['LT']))][:10]
for i in range(len(top)):
    print(top[i][0],top[i][1],top[i][2],top[i][3],round(float(top[i][4])*100, 2),'din care de pe altceva decat liste permanente:',round(float(top[i][5])*100, 2))

# Procent vot de pe liste permanente
total = 0
total_permanent = 0
for sectie in sectii:
    total_permanent += int(sectie['LP'])
    total += int(sectie['LT'])
print('\n[*] Procent vot de pe liste permanente:', total_permanent/total*100)

luku = input('Anna luku: ')
pienin=suurin=float(luku)
while luku!='lopeta.':
    if luku == "":
        break
    print('Kiitos.')
    luku=float(luku)
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku
    luku = input('Anna luku:')
print(f'Pienin antamasi luku on: {pienin}')
print(f'Suurin antamasi luku on: {suurin}')
print('Havisit pelin, hyvasti.')

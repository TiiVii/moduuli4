luku = float(input('Anna tuuma maara: '))

while luku!='lopeta.':
    if luku < 0:
        break
    tulos = luku * 2.54
    print(f'{luku} tuuma on {tulos:.2f} senttimetria.')
    luku = float(input('Anna tuuma maara: '))
print('Toiminnan lopetus. Hyvasti.')


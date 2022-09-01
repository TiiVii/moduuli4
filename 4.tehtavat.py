from random import randint

onnenluku = randint(1,10)

arvaus = input('Heita arvaus onnenluvusta: ')

while arvaus!=onnenluku:
    if arvaus == onnenluku:
        break
    arvaus=float(arvaus)
    onnenluku=float(onnenluku)
    if arvaus < onnenluku:
        print('Arvauksesi on pienempi kuin onnenluku.')
    if arvaus > onnenluku:
        print('Arvauksesi on suurempi kuin onnenluku.')
    if arvaus!=onnenluku:
        arvaus = input("Hieno veikkaus, yritappa uudestaan: ")
print('Onneksi olkoon, arvasit oikein!')

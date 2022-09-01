import math
import random

N = 0
n = 0

while True:
    try:
        kaikkipisteet = int(input('Anna pistemaara: '))
    except ValueError:
        print('Anna pistemaara numeromuodossa.')
    else:
        if kaikkipisteet == 0:
            print("Pistemaaran tulee olla suurempi kuin nolla.")
        elif kaikkipisteet < 0:
            print("Pistemaaran tulee olla positiivinen luku.")
        else:
            break

while N < kaikkipisteet:
    point: tuple[float, float] = (random.uniform(-1, 1), random.uniform(-1, 1))
    if point[0] ** 2 + point[1] ** 2 < 1:
        n += 1
    N += 1
   print(kaikkipisteet-N)

print(f"Estimation: {(4*n)/kaikkipisteet:.5f}")
print(f"True value: {math.pi:.5f}")
n = 1
minn = 3
maxn = 999

def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n



while eka <= 3:
    toka = 3
    while toka <= 999:
        print(f'Kolmella jaolliset luvut valilla {eka} ja 1000 ovat: {eka * toka:d}')
        toka = toka + 1
    eka = eka + 1
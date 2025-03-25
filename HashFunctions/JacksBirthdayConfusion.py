from math import factorial

m = 2 ** 11
p = 0.75
for n in range(2, 200):
    res = 1 - (factorial(m) / (factorial(m - n) * m ** n))
    if p - 0.01 < res < p + 0.01:
        print(f"{n=}: {res:.04}")
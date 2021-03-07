from time import time
import math

def potenciaperfecta(n):
    log2 = int(math.floor(math.log(n, 2.0)))
    a = 0
    for i in range(2,log2):
        a = n ** (1./i)
        if a.is_integer() is True:
            print('El numero es compuesto')


def mcd(n, r):
    mayor = max(n, r)
    menor = min(n, r)
    a = mayor % menor
    while (a > 0):
        mayor = a
        a = menor%a
        menor = mayor
    return menor



def app():
    n = int(11)
    result = potenciaperfecta(n)
    maximo = mcd(11, 7)
    print (maximo)

if __name__ == '__main__':
    app()

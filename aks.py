from time import time
import math

def isPrime(r):
    raiz = int(sqrt(r)) + 1
    for i in range(2,raiz):
        if r % i == 0:
            return False
    return True

def factor(r):
    for i in range(2, r - 1):
        if(r % i == 0):
            a = i
    print(a)
    return a

def potenciaperfecta(n):
    log2 = int(math.floor(math.log(n, 2.0)))
    a = 0
    for i in range(2,log2):
        a = n ** (1./i)
        if a.is_integer() is True:
            print('COMPOSITE')

def mcd(n, r):
    mayor = max(n, r)
    menor = min(n, r)
    a = mayor % menor
    while (a > 0):
        mayor = a
        a = menor%a
        menor = mayor
    return menor

def orden (n, r):
    exp = int(1)
    min = math.log(n, 2.0) ** 2
    print(min)
    a = 0.0
    
    for i in range (0,50):
        a = (n**exp)
        a = a - 1
        a = a % r
        print ('a vale', a)
        if a == 0:
            if exp > min:
                print('El orden es ', r)
                return 0
            else:
                r = r + 1
                exp = exp + 1
                print('El orden vale ', r)
                print('El exp es ', exp)
        else:
            exp = exp + 1
            print('El exp es ', exp)
        

def app():
    n = int(5)
    r = int(3)
    a = orden(n, r)

  
                
if __name__ == '__main__':
    app()

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
            return True

def totient(n):
    phi = 0
    for i in range(1,n):
        if (mcd (i,n) == 1):
            phi = phi + 1
    return phi
        

def mcd(n, r):
    mayor = max(n, r)
    menor = min(n, r)
    a = mayor % menor
    while (a > 0):
        mayor = a
        a = menor%a
        menor = mayor
    return menor

def orden (n):
    r = int(3)
    exp = int(1)
    min = math.log(n, 2.0) ** 2
    a = 0.0
    while (r < n):
        a = (n**exp)
        a = a - 1
        a = a % r
        if a == 0:
            if exp > min:
                return r
            else:
                r = r + 1
                exp = exp + 1
        else:
            exp = exp + 1
    return 0    

#def condicionSuf(n, r):
 #   phi = totient(r)
  #  limite = int(math.sqrt(phi))*math.log(n)


def app():
    start_time = time() 
    n = int(9)
    phi = totient(n)
    print ('Phi de n es ', phi)
    print ('Evaluando si ',n,'es potencia perfecta')
    if potenciaperfecta(n) is True:
        print ('COMPOSITE')
    else:
        print('El numero no es potencia perfecta, evaluando r minimo')
        b = orden(n) 
        if b > 0:
            print ('El minimo r es ', b)
            if mcd (n,b) > 1:
                print ('COMPOSITE')
            else:
                print (n, "es primo")
        else:
            print (n, "es primo")
    elapsed_time = time() - start_time
    print('Tiempo de ejecucion en segundos',elapsed_time)   
                
if __name__ == '__main__':
    app()

import math
import time
import matplotlib.pyplot as plt

## Formule de récurrence

def fibo_table(n):
    """ Retourne le nombre F_n (méthode itérative avec tableau) """
    f = [0, 1]
    for k in range(2,n+1):
        f.append(f[k-1] + f[k-2])
    return f[n]
    
def fibo(n):
    """ Retourne le nombre F_n (méthode itérative sans tableau """
    if n == 0 or n == 1:
        return n
    u, v = 0, 1
    for i in range(2, n+1):
        s = u + v
        u = v
        v = s
    return s

## Formule explicite

def fibo_binet(n):
    """ Retourne le nombre F_n (méthode avec la formule de Binet) """
    phi, phib = (1 + math.sqrt(5))/2, (1 - math.sqrt(5))/2
    f = (phi**n - phib**n)//math.sqrt(5)
    
    return int(f) # Attention à l'exponentiation de phi et phib
    


## Algo récursif

def fiborec(n):
    """ Retourne le nombre F_n (tentative récursive) """
    if n == 0 or n == 1:
        return n
    else:
        return fiborec(n-1) + fiborec(n-2) # Attention aux calculs inutiles

## Ecriture matricielle (expo rapide)

def exporaprec(a,n):
    """ Fonction retournant a^n  (exponentation rapide récursive) """
    if n == 0:
        return 1
    elif n % 2 == 0:
        return exporap(a**2, n/2)
    else:
        return a*exporap(a**2, (n-1)/2)

def exporapiter(a,n):
    """ Fonction retournant a^n  (exponentation rapide itérative) """
    exposant = n
    itere = a
    produit = 1
    while exposant != 0:
        if n % 2 != 0:
            produit = itere * produit
            exposant = exposant - 1
        else:
            itere = itere * itere
            exposant = exposant/2
    return produit

## Ecriture matricielle (algo)

def proMat(A, B):
    """ Fonction renvoyant le produit matriciel de 2 matrices A et B """
    n, p, q = len(A), len(A[0]), len(B[0])
    return [[sum([A[i][k]*B[k][j] for k in range(p)]) for j in range(q)] for i in range(n)]


A = [[0, 1], [1, 1]] # Matrice A

def fibo_exporap(A, n):
    """ Fonction retournant A^n (exponentation rapide récursive matricielle) """
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n % 2 == 0:
        return fibo_exporap(proMat(A, A), n/2)
    else:
        return proMat(A, fibo_exporap(proMat(A, A), (n-1)/2))



## Création du graphique de comparaison

def graphique():
    Yfibo = []
    Yfibo_expo = []
    N = [10, 100, 1000, 10000, 15000, 20000, 30000, 40000, 50000, 70000, 80000, 100000, 200000, 300000, 400000, 500000, 600000, 800000, 10**6]
    for n in N:
        debut1 = time.time()
        a = fibo(n)
        Yfibo.append(time.time() - debut1)
        
        debut2 = time.time()
        b = fibo_exporap(A, n)
        Yfibo_expo.append(time.time() - debut2)
    
    plt.plot(N, Yfibo, 'r-', label="fibo")
    plt.plot(N, Yfibo_expo, 'g-',label="fibo_exporap")
    
    plt.legend()
    plt.title("Comparaison des différentes méthodes de calcul de $F_n$")
    plt.xlabel("Nombres de Fibonacci calculés")
    plt.ylabel("Durée (en sec)")
    plt.ylim(0,160)
    plt.show()


## Euclide (non traité MAIS à tester)

def euclide(a, b):
    """ Algorithme d'Euclide itératif """
    u, v = a, b
    while v != 0:
        r = u % v
        u = v
        v = r
    return u

def eucliderec(a, b):
    """ Algorithme d'Euclide récursif """
    if b == 0:
        return a
    else:
        return eucliderec(b, a % b)

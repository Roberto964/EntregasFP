'''
Created on 17 oct 2024

@author: rober
'''
from math import factorial

def Ejercicio1(n:int,k:int)->int:
    if n > k :
        i:int = 0
        r:int = 1
        for i in range(0,k):
            r = (n-i+1)*r
        return r 
    else :
        return (int(f"El numero {n} es menor a {k} por tanto es imposible su cálculo"))
  

def Ejercicio2(a1:int, r:int, k:int)->int:
    an:float = 1
    for i in range(0,k):
        an = a1 * r**(i)*an
    return (int(an))
        
    
   
def Ejercicio3(n:int, k:int)->float:
    if n >= k :
        w = factorial(n)/((factorial(k))*(factorial(n-k)))
    return (w)
    
def Ejercicio4(n:int, k:int)->float:
    suma:int = 0
    if  n >= k :
        for i in range(0,k): 
            x:float = (-1)**i
            y:float = factorial(k+1)/(factorial(i+1)*factorial((k+1) - (i+1)))
            z:float = (k - i)**n
            m:float = 1/factorial(k)
            suma +=int(x*y*z)
            s:float = float(m * suma)
    else:
        return(float(f"No hemos podido calcular a causa de que {k} es mayor que {n} en este caso."))
    
    return(s)

def Ejercicio5(a,ep)-> float:
    f = lambda x : 2*(x**2)
    
    fd = lambda x : 4*x

    while (abs(f(a))>ep):
        a = a - (f(a)/fd(a))
    return a






        
    


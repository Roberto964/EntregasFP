'''
Created on 17 oct 2024

@author: rober
'''
from math import factorial


def P2(n:int,k:int,i:int=1):
    assert n>0,'debe ser positivo'
    assert k>0,'debe ser positivo'
    assert i >0, 'debe ser positivo'
    assert i<k+1,'debe ser mayor i a k+1'
    assert n>k
    r:int = 1
    for i in range(1,k-1+1):
            r = (n-i+1)*r
    return r 
  
def C2(n:int, k:int)->float:
    assert k>0,'debe ser positivo el numero k'
    assert n>0,'debe ser positivo el numero n'
    if n >= k :
        w = factorial(n)/((factorial(k+1))*(factorial(n-(k+1))))
    return (w)

def S2(n:int, k:int)->float:
    suma:int = 0
    if  n >= k :
        for i in range(0,k+1): 
            x:float = (-1)**i
            y:float = factorial(k)/(factorial(i)*factorial((k) - (i)))#
            z:float = (k - i)**(n+1)
            m:float = factorial(k)/(n*factorial(k+2))#
            suma +=int(x*y*z)
            s:float = float(m * suma)
    else:
        return(float(f"No hemos podido calcular a causa de que {k} es mayor que {n} en este caso."))
    
    return(s)

def palabrasMasComunes(fichero,n=5)->list[tuple[str, int]]:
    assert n>1,'n debe ser mayor que 1'
    with open(fichero, 'r' ,encoding = 'utf-8') as f:
        ls:list[str]=[]
        numero:int=0
        for linea in f:
            for i in linea.split(' '):
                if i.lower() == i.lower():
                    numero+=(int(i))
                    n=(i,numero,)
                    ls.append(n.strip())
                    
        return ls






if __name__ == '__main__':

    print(P2(4,2))
    print()
    print(C2(4, 2))
    print()
    print(S2(4, 2))
    print()
    print((palabrasMasComunes('../../resources/archivo_palabras.txt.txt', '5')))
'''
Created on 11 nov 2024

@author: rober
'''
from Entrega2.Clases import Lista_ordenada

def test_LO1():
    order=lambda x:x
    laLista=Lista_ordenada(order)
    laLista.add(3)
    laLista.add(1)
    laLista.add(2)
    print(f'Nuestra lista va a ser: {laLista._elements}')
    laLista.remove()
    print(f'Nuestra lista con remove: {laLista._elements}')
    
def test_LO3():
    order=lambda x:x
    laLista=Lista_ordenada(order)
    laLista.add(3)
    laLista.add(1)
    laLista.add(2)
    print(f'Nuestra lista con remove_all: {laLista.remove_all()}')

def test_LO4():
    order=lambda x:x
    laListe=Lista_ordenada(order)
    laListe.add(3)
    laListe.add(1)
    laListe.add(2)
    laListe.add(0)
    print(f'Añadiendo el 0 : {laListe._elements}')
    laListe.add(10)
    print(f'Ahora el 10: {laListe._elements}')
    laListe.add(7)
    print(f'Y el 7 : {laListe._elements}')
    

if __name__ == '__main__':
    
#############################################################
    test_LO1()
#############################################################
    test_LO3()
#############################################################
    test_LO4()
#############################################################
    
    
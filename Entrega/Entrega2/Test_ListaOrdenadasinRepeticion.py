'''
Created on 11 nov 2024

@author: rober
'''
from Entrega2.Clases import Lista_ordenada, Lista_ordenada_sin_repeticion

def test_LO1():#23, 47, 47, 1, 2, -3, 4, 5
    order=lambda x:-x
    laLista=Lista_ordenada_sin_repeticion(order)
    laLista.add(23)
    laLista.add(47)
    laLista.add(47)
    laLista.add(1)
    laLista.add(2)
    laLista.add(-3)
    laLista.add(4)
    laLista.add(5)
    print(f'Nuestra lista va a ser: {laLista._elements}')
    laLista.remove()
    print(f'Nuestra lista con remove: {laLista._elements}')
    
def test_LO3():
    order=lambda x:-x
    laLista=Lista_ordenada_sin_repeticion(order)
    laLista.remove_all()
    print(f'Nuestra lista con remove_all: {laLista._elements}')

def test_LO4():
    order=lambda x:-x
    laListe=Lista_ordenada_sin_repeticion(order)
    laListe.add(23)
    laListe.add(47)
    laListe.add(47)
    laListe.add(1)
    laListe.add(2)
    laListe.add(-3)
    laListe.add(4)
    laListe.add(5)
    print(f'Nuestra lista sin añadir nada resultaría : {laListe._elements}')
    laListe.add(0)
    print(f'Añadimos el 0 : {laListe._elements}')
    laListe.add(10)
    print(f'Añadimos el 10 : {laListe._elements}')
    laListe.add(7)
    print(f'Añadimos un 7 : {laListe._elements}')
    

if __name__ == '__main__':
    
#############################################################
    test_LO1()
#############################################################
    test_LO3()
#############################################################
    test_LO4()
#############################################################
    
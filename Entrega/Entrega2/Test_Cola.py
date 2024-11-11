'''
Created on 11 nov 2024

@author: rober
'''

from Entrega2.Clases import Cola

def test_C1():
    col=Cola()
    col.add_all([23, 47, 1, 2, -3, 4, 5])
    print(f'La cola tras añadirle todos los elementos es:{col._elements}')

def test_C2():
    col=Cola()
    col.add_all([23, 47, 1, 2, -3, 4, 5])
    print(f'La cola tras retirarle todos los elementos es:{col.remove_all()}')

if __name__ == '__main__':
    test_C1()
    test_C2()
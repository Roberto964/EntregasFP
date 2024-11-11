'''
Created on 3 oct 2024

@author: rober
'''
from lecturas.lecturas import *
    
if __name__ == '__main__':
    
##################################################################

    print(f'El número de veces que aparece la palabra quijote en el fichero lin_quijotes: ')
    print(Lecturas1('../../resources/lin_quijote.txt','Quijote'))
    print()
##################################################################

    print(f'Las líneas en las que aparece la palabra quijote son: ')
    print(Lecturas2('../../resources/lin_quijote.txt','Quijote'))
    print()
##################################################################

    print(f'Las palabras únicas en el fichero archivo_palabras son: ')
    print(Lecturas3('../../resources/archivo_palabras.txt'))
    print()
##################################################################

    print(f'La longitud promedio de las líneas del fichero palabras_random es: ')
    print(longitud_promedio_lineas('../../resources/palabras_random.csv'))
    print()
##################################################################

    print(f'La longitud promedio de las líneas del fichero resources/vacio es:  ')
    print(longitud_promedio_lineas('../../resources/vacio.csv'))

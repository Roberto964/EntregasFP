'''
Created on 17 oct 2024

@author: rober
'''

def Lecturas1(file:str, cad:str):
    separador:str=(' ')
    acum:int=0
    with open(file, 'r', encoding ='utf-8') as f:
        for linea in f:
            palabra:list[str] = linea.split(separador)
            for i in palabra:
                if i.lower() == cad.lower():
                    acum+=1
        return acum
    
def Lecturas2(file, cad:str):
    with open(file, 'r' ,encoding = 'utf-8') as f:
        ls:list[str]= []
        for linea in f:
            for palabra in linea.split(' '):
                if palabra.lower() == cad.lower():
                    ls.append(linea.strip())
    return ls

def Lecturas3(file):
    with open(file, 'r' ,encoding = 'utf-8') as f:
        ls:list[str]=[]
        for linea in f:
            for i in linea.split(' '):
                if i == i:
                    ls.append(i.strip())
                    cj=set(ls)
                    lt=list(cj)
    return lt

def longitud_promedio_lineas(file_path: str):#en este ejercicio debemos medir la longitud de cada uno de las lineas y calcular su valor medi, es decir, dividirlo entre 2
    sep:str =(',')
    suma_de_palabras:int=0
    lineas:int= 0
    with open(file_path, encoding='utf-8') as f:
        for linea in f:
            lineas+=1
            for i in linea.split(sep):
                if i == i :
                    suma_de_palabras+=1
        try:
            return(suma_de_palabras/lineas)
        except ZeroDivisionError:
            return (None)
            
            



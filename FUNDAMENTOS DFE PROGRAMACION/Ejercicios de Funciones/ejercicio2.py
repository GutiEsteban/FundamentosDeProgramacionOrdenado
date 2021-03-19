# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:34:12 2021

@author: gutie
"""
# Practicando funciones

def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


def separacion():
    print("*******************************")    


# programa principal

for x in range(5):
    carga_suma()
    separacion()
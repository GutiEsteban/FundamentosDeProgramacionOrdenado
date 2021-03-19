# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:48:15 2021

@author: gutie
"""

# Practicando funciones
def calcular_producto():
    valor1=int(input("Ingrese el primer valor: ") )
    valor2=int(input("Ingrese el segundo valor : "))
    producto=valor1*valor2
    print("El producto de los valores es : ",producto)
    


def calcular_cuadrado():
    
    valor=int(input("Ingrese un numero entero : "))
    cuadrado=valor*valor
    print("El valor de cuadrado es : ",cuadrado)



# Panel principal
calcular_cuadrado()
calcular_producto()
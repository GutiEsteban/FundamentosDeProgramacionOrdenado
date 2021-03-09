# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 10:54:27 2021

@author: gutie
"""

# Programa que calcula el cuadro de los primeros 100 numeros (Ciclo while)
# Declaracion de variables
contadorRepeticiones=1
cuadradoNum=0
acumuladorSuma=0
cantidadElementos=int(input("ingrese la cantidad de elementos que desea elevar al cuadrado : "))

while  contadorRepeticiones<=cantidadElementos:
    cuadradoNum=pow(contadorRepeticiones,2)
    print("El cuadrado es : ",cuadradoNum)
    acumuladorSuma+=cuadradoNum
    print("El acumulador de la suma es : ",acumuladorSuma)
    contadorRepeticiones=contadorRepeticiones+1
#Fin while

#Salida
print("La suma de los cuadrados es : ",acumuladorSuma)
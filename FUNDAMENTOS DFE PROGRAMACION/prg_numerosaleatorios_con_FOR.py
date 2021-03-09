# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:38:42 2021

@author: gutie
"""

#HACER ESTO CON EL CICLO FOR




#Librerias usadas 
import random
#Ejercicio 2

# Declaramos variables
cantidadNumeros=1
num=0
acumuladorSumaTodosNumeros=0
acumuladorSumaNumerosPositivos=0
acumuladorSumaNumerosNegativos=0

#Entradas
cantidadNumeros=int(input("Cantidad de numeros : "))
#Proceso 
for num in range (cantidadNumeros):
    numero=random.randint(-100,100) # Generamos Numeros 
    print(numero)
    acumuladorSumaTodosNumeros+=numero
    if numero>0:
        acumuladorSumaNumerosPositivos=acumuladorSumaNumerosPositivos+numero
    else:
        acumuladorSumaNumerosNegativos=acumuladorSumaNumerosNegativos+numero
#Fin del ciclo

#salida de resultados
print("La suma de todos los numeros es: ",acumuladorSumaTodosNumeros)
print("La suma de todos los numeros positivos es: ",acumuladorSumaNumerosPositivos)
print("La suma de todos los numeros negativos  es: ",acumuladorSumaNumerosNegativos)

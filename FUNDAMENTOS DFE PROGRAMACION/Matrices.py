# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 10:44:50 2021

@author: gutie
"""

# Matrices 

# 1. Declarar la matriz

matrizNumeros=[[12,32,56,48],[8,48,18,58],[2,4,6,8]]

# 2. Imprimimos la matriz

print(matrizNumeros)

# 3. Imprimir una posicion fija

print("Posicion especifica : ",matrizNumeros[0][2]) 

# 4. Solicitar la posicion al usuario
fil=int(input("Fila : "))
col=int(input("Columna : "))
print("Posicion leida por teclado : ",matrizNumeros[fil-1][col-1])
# 5. Imprimir fila determinada 

print("Fila 0 :  ",matrizNumeros[0])

print("Fila 1 :  ",matrizNumeros[1])

# 6. Imprimir una columna
for f in range (3):
    print(matrizNumeros[f][1])
    
# 7. Imprimir la columna que el usuario elija

col=int(input("Columna que deseo imprimir : "))
for f in range (3):
    print(matrizNumeros[f][col])

# 8.  Sumar todos los elementos de la matriz 
sumEleMat=0
for f in range (3):
    for c in range (4):
        sumEleMat=sumEleMat+matrizNumeros[f][c]
print("La suma de los elementos es : ",sumEleMat)

# 9. Sumar e imprimir los elementos de cada fila 
print("Sumar e imprimir la suam de los elementos d euna fila :D ")
sumEleMat=0
for f in range (3):
    for c in range (4):
        sumEleMat=sumEleMat+matrizNumeros[f][c]
    print("La suma de los elementos es : ",sumEleMat)
    sumEleMat=0
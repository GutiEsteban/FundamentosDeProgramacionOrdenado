# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:06:35 2021

@author: gutie
"""

# Declarar la estructura tipo lista vacia

listaNotas=[]

# Almacenar datos en la lista

for posVec in range (10):
    # Leemos la nota de un estudiante 
    notaEstudiante=float(input("Digite nota : "))
    # Adicionamos la nota a la lista 
    listaNotas.append(notaEstudiante)
    

#Imprimir la lista 
print(listaNotas)


# Declarar una variable para almacenar la suma 
sumaNotas = 0.0
# Recorrer el arreglo e ir acumulando en la variable

for x in range (len( listaNotas)):
    sumaNotas=sumaNotas+listaNotas[x]

print("Suma : ",sumaNotas)
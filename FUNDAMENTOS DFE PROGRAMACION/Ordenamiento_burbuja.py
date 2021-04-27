# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 10:21:20 2021

@author: gutie
"""

# Ordenamiento burbuja 

# Definicion del vector
#listaEnteros=[35,39,643,786,123]
listaEnteros=[]

def pedirDatos(listaEnteros):
    print("----------Cargando los datos ------------")
    for h in range (4):
        valor=int(input("Ingrese los valores de la lista : "))
        listaEnteros.append(valor)
    print(listaEnteros)    
# Funcion que realiza el ordenamiento burbuja

def ordBurbuja (listaDesordenada):
    print("---------Ordenar datos------------")
    for k in range(1,len(listaDesordenada)-1):
        for l in range(0,len(listaDesordenada)-1):
            if listaDesordenada[l]>listaDesordenada[l+1]:
                aux=listaDesordenada[l]
                listaDesordenada[l]=listaDesordenada[l+1]
                listaDesordenada[l+1]=aux

# Fin del ordenamiento

# Llamamos la funcion 
pedirDatos(listaEnteros)
ordBurbuja(listaEnteros)

print(listaEnteros)
            
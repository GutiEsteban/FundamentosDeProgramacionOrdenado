# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:36:08 2021

@author: gutie
"""

#practicando fun ciones
def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese valor:"))
        lista.append(valor)
    return lista


def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x], end=",")


# bloque principal

lista=cargar()
imprimir(lista)
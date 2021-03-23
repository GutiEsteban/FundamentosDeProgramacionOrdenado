# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:35:46 2021

@author: gutie
"""

#Practicando funciones 
def calcular_sueldo(nombre,costohora,cantidadhoras):
    sueldo=costohora*cantidadhoras
    print(nombre,"trabajo",cantidadhoras,"y cobra un sueldo de",sueldo)


# bloque principal

calcular_sueldo("juan",10,120)
calcular_sueldo(costohora=12,cantidadhoras=40,nombre="ana")
calcular_sueldo(cantidadhoras=90,nombre="luis",costohora=7)
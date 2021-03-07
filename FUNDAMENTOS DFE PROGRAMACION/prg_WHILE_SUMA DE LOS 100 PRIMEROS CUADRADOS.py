# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 13:16:16 2021

@author: gutie
"""

#Escribir un programa que calcule la suma de los cuadrados de los 100 primeros números enteros.(con WHILE)

n=0
suma=0
while n<100:
    n=n+1
    ope=n*n
    suma=suma+ope
print("La suma es :",suma)
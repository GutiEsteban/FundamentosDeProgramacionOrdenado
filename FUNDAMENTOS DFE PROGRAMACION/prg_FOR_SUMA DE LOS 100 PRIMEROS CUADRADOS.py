# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:23:37 2021

@author: gutie
"""

 #Escribir un programa que calcule la suma de los cuadrados de los 100 primeros números enteros.(con FOR)
n=1
suma=0
for i in range (1,101):
    n=i*i
    suma=suma+n
print ("la suma es : ",suma)
 
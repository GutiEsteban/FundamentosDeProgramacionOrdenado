# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:27:56 2021

@author: gutie
"""


#2.  Escribir un programa que genere aleatoriamente 100 datos
# y sume todos los números, los negativos, los positivos y calcule 
#el pmedio de todos los números, de los positivos y los negativos; además que calcule el mayor y 
#el mroenor de todos los números, de los positivos y los negativos
import random 
num=0
resta=0
sumaT=0
i=0
radint=0
suma=0
pro1=0
pro2=0
mayor=0
for i in range (100):
    num=random.randint(-50,50)
    print(num)
    if num>0:
        suma=suma+num
    else :
        resta=resta+num
print("Su suma es : ",suma,"Su resta es : ",resta)
sumaT=(resta+suma)/100
print("El promedio es : ",sumaT)
pro1=suma/100
pro2=resta/100
print("El promedio de la suma es  : ",pro1,"El promedio de la resta  es : ",pro2)

mayor=max(sumaT)
print("El numero mayor de todos los numeros aleatorios es : ",mayor)

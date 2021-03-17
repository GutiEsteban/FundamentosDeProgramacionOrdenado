# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:44:03 2021

@author: gutie
"""

# Programa que calcula la hipotenusa y el perimetro de un triangulo rectangulo


# Declaracion y llamado a las librerias y paquetes 
import math

def f_titulo():
    print("Calculo de la hipotenuza de un triangulo rectangulo")

def f_calcularHipotenusa():
# Variables
    ve_catetoUno = 0.0  
    ve_catetoDos = 0.0
    
    vp_radicando = 0.0
    
    vps_hipotenusa = 0.0
    #vps_perimetro = 0.0
    
    # Entradas
    ve_catetoUno = int(input("Ingrese el primer cateto :" ))
    ve_catetoDos = int(input("Ingrese el segundo cateto : "))
    
    # Proceso
    vp_radicando = math.pow(ve_catetoUno, 2)+math.pow(ve_catetoDos, 2)
    vps_hipotenusa = math.sqrt(vp_radicando)
    
    # Salidas
    
    print ("Hipotenusa",vps_hipotenusa)   
# Fin del desarrollo de la funcion

# Llamado de la funcion

f_titulo()  
f_calcularHipotenusa()
  
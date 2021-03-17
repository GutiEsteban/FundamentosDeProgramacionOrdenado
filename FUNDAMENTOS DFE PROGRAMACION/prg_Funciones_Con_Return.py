# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:27:21 2021

@author: gutie
"""

# Programa que calcula la hipotenusa y el perimetro de un triangulo rectangulo


# Declaracion y llamado a las librerias y paquetes 
import math

# Declaracion e Inicializacion de Variables
ve_catetoUno = 0.0  
ve_catetoDos = 0.0

def f_titulo():
    print("Calculo de la hipotenusa de un triangulo rectangulo")


def f_calcularHipotenusa(p_catetoUno,p_catetoDos):
 
    vp_radicando = 0.0
    
    vps_hipotenusa = 0.0
    #vps_perimetro = 0.0
    
    
    
    # Proceso
    vp_radicando = math.pow(p_catetoUno, 2)+math.pow(p_catetoDos, 2)
    vps_hipotenusa = math.sqrt(vp_radicando)
    
    # Retornar la respuesta
    return vps_hipotenusa

# Fin del desarrollo de la funcion
def f_despedida():
    print("**** Gracias por usarme ,adiós ****")
# Control del programa -PRINCIPAL-
f_titulo()
ve_catetoUno = int(input("Ingrese el primer cateto :" ))
ve_catetoDos = int(input("Ingrese el segundo cateto : "))

vps_rf_hip = f_calcularHipotenusa(ve_catetoUno,ve_catetoDos)
print("La hipotenusa es : ",vps_rf_hip)
f_despedida()
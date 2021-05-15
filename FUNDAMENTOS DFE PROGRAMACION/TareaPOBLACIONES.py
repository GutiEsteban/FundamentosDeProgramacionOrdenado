# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:26:27 2021

@author: gutie
"""

# Importo libreria 

import pandas as pd 

# Variables 

archivoExcel = pd.read_excel('Departamentos.xlsx')

Poblacion=archivoExcel['Poblacion']

Ndepartamentos = archivoExcel['Departamento']

area=archivoExcel['Superficie']

# Funciones 

def calcularArea():
    areaT=0
    for a in area:
        areaT=areaT+ (a)
    return(areaT)


def SumaPoblacion():
    poblacionT=0
    for a in Poblacion:
        poblacionT=poblacionT+ (a)
    return(poblacionT)


def PromedioPoblacion():
    PromedioDePoblacion= SumaPoblacion()/len(Ndepartamentos)
    return(PromedioDePoblacion)
        
def PromedioAreaPorDep():
    promedioAreaDep= calcularArea()/len(Ndepartamentos)
    return(promedioAreaDep)


menoramayor=archivoExcel.sort_values(by=['Poblacion'],ascending=[False]) 


    
Relacion=Poblacion*area   



# Llamar funciones e impresiones  


print("EL Area total es  : ",calcularArea())

print("El promedio de la poblacion por departamento es : ",PromedioPoblacion())

print("El promedio de area por departamento es : ",PromedioAreaPorDep())

print("----------------Departamentos ordenados de mayor a menor poblacion --------------",menoramayor)
print("------------------------------")
print("--------------Relacion habitantes territorio----------------",Relacion)


#------------------------------------------------------------------------------------------------

# Importamos libreria 

import matplotlib 
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
ax.set_title("Departamento y Poblacion")
ax.set_ylabel("Poblacion")
ax.set_xlabel("Departamento")
#crear el gráfico
plt.bar(Ndepartamentos,Poblacion)
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:16:11 2021

@author: gutie
"""

# Interactuar cpn datos
# Fuentes de Datos 
# 1. Asignar los datos desde la definicion de la estructura 
# Importamos la librerias 
import pandas as pd

# Crear la estructura de datos tipo dataframe y se le asignan los datos

datosEstudiantes = pd.DataFrame({'Estudiante ':['Juan','Ana','Marta'],
                                 'Apellido':['Gomez','Dias','Arango'],
                                 'Edad':[18,25,17]})
# Agregar una columna y le asignamos el mismo dato

datosEstudiantes['Vivo']='TRUE'
datosEstudiantes['Genero']='Masculino'


# Insertar una columna  y se asignan los datos 

datosEstudiantes.insert(4,'Semestre',['Primero','Quinto','Noveno'])

datosEstudiantes.insert(6,'Genero correcto',['Masculino','Femenino','Femenino'])

# Segunda manera de agregar una columna   sobreescribiendo
datosEstudiantes = datosEstudiantes.assign(Colegio = ['Nuestra señora','Mexico City','Chuchunco City'])

# Consultar la estructura
print(datosEstudiantes)
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:06:35 2021

@author: gutie
"""

# Declarar la estructura tipo lista vacia

listaNotas=[]
n=int(input("Ingrese la cantidad de estudiantes : "))

# Almacenar datos en la lista

for posVec in range (n):
    # Leemos la nota de un estudiante 
    notaEstudiante=float(input("Digite nota : "))
    # Adicionamos la nota a la lista 
    listaNotas.append(notaEstudiante)
    

#Imprimir la lista 
print(listaNotas)


# Declarar una variable para almacenar la suma 
sumaNotas = 0.0
# Recorrer el arreglo e ir acumulando en la variable

for x in range (len( listaNotas)):
    sumaNotas=sumaNotas+listaNotas[x]

print("Suma : ",sumaNotas)

for x in range(len(listaNotas)):
    promedio=sumaNotas/len(listaNotas)
print("El promedio de notas es  : ", promedio)

posicion2=0
mayor=listaNotas[0]
for x in range(n):
    if listaNotas[x]>mayor:
        mayor=listaNotas[x]
        posicion2=x

print("Mayor de la lista :",mayor )
print("Posicion del mayor en la lista : ",posicion2)


menor=listaNotas[0]
posicion=0
for x in range(n):
    if listaNotas[x]< menor:
        menor=listaNotas[x]
        posicion=x


print("Menor de la lista : ",menor)

print("Posicion del menor en la lista : ",posicion)

Aprobaron =0
Reprobaron =0
for x in range(len(listaNotas)):
    if listaNotas[x]>=3:
        Aprobaron= Aprobaron + 1
        
    else:
        Reprobaron=Reprobaron +1
print (" La cantidad de estudiantes que reprobaron son: ",Reprobaron)
print (" La cantidad de estudiantes que aprobaron son: ",Aprobaron)
uno=0
dos=0
tres=0
cuatro=0
cinco=0
for x in range(len(listaNotas)):
    if 0 <= listaNotas[x] <= 1:
        uno= uno+1
    if 1.1 <= listaNotas[x] <= 2:
        dos= dos+1
    if 2.1 <= listaNotas[x] <= 3:
        tres= tres+1
    if 3.1 <= listaNotas[x] <= 4:
        cuatro= cuatro+1
    if 4.1 <= listaNotas[x] <= 5:
        cinco= cinco+1
print("El numero de almunos entre 0 y 1 es : ",uno)
print("El numero de almunos entre 1.1 y 2 es : ",dos)
print("El numero de almunos entre 2.1 y 3 es : ",tres)
print("El numero de almunos entre 3.1 y 4 es : ",cuatro)
print("El numero de almunos entre 4.1 y 5 es : ",cinco)

   
        




        
    
            
  
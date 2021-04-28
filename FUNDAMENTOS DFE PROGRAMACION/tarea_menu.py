# -*- coding: utf-8 -*-
import os
def menu():
    os.system('cls')
    print('Selecciona una opción')
    print("\t1 - Cargar lista")
    print('\t2 - Ordenamiento Burbuja')
    print("\t3 - Ordenamiento Inserción")
    print('\t4 - Ordenamiento Shell')
    print('\t9 - Salir')
def burbuja(lista):
    i = 1
    while i == 1:
        i = 0
        for x in range(len(lista)-1):
            if lista[x] > lista[x+1]:
                aux = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = aux
                i=1
    print('Ordenamiento Burbuja: ', lista)
def insercion(lista):
    for x in range(1, len(lista)):
        n = lista[x]
        i = x-1
        while i >= 0 and n < lista[i]:
            lista[i+1] = lista[i]
            i = i-1
        lista[i+1] = n            
    print('Ordenamiento inserción: ', lista)
def ord_shell(lista):
    n=len(lista)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = lista[i]
            j = i
            while j >= interval and lista[j - interval] > temp:
                lista[j] = lista[j - interval]
                j -= interval

            lista[j] = temp
        interval //= 2
    print('Ordenamiento Shell',lista)

lst = []

while True:
    menu()
    opcionMenu = input("inserta un numero valor >> ")
    if opcionMenu=='1':
        lst = []
        x = int(input('Numero de datos en la lista: '))
        for i in range(x):
            num = int(input('Ingrese número: '))
            lst.append(num)
        print(lst)
    elif opcionMenu=='2':
        burbuja(lst)
    elif opcionMenu=='3':
        insercion(lst)
    elif opcionMenu=='4':
       ord_shell(lst)     
    elif opcionMenu=='9':
        break
    else:
        input('No has pulsado ninguna opción correcta. Pulsa una tecla para continuar')
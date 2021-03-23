# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:36:51 2021

@author: gutie
"""

#Practicando funciones
def sumar(v1, v2, v3):
    return v1 + v2 + v3

li=[2, 4, 5]
su=sumar(*li)
print(su)
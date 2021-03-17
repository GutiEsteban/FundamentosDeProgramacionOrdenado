# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:13:53 2021

@author: gutie
"""

# Calculo d ela combinatoria de 2 numeros M,N

ve_M = int(input("Digite M : "))
ve_N = int(input("Digite N : "))
fact_M = 1
fact_N = 1
fact_MN = 1


# Calcular el factorial de M
for i in range (1,ve_M+1,1):
    fact_M = fact_M*i

# Calcular el factorial de N
vp_conRepWhile = 1
while(vp_conRepWhile<=ve_N):
    fact_N=fact_N*vp_conRepWhile
    vp_conRepWhile=vp_conRepWhile+1

# Calcular el factorial de M-N
vp_difMN = ve_M-ve_N

for j in range (1,vp_difMN+1,1):
    fact_MN = fact_MN*j

# Calcular la Combinatoria 
vps_comb_MN = fact_M/(fact_N*fact_MN)
    


# Salidas
print("El factorial de M es : ",fact_M)
print("El factorial de N es : ",fact_N)
print("Factorial de M-N : ",fact_MN)
print("La combinatoria de M,N : ",vps_comb_MN)
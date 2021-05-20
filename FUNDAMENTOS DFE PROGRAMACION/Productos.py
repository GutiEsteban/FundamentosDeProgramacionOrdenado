# -*- coding: utf-8 -*-
"""
Created on Thu May 20 10:19:30 2021

@author: gutie
"""

import pandas as pd

df_archivoExcel = pd.read_excel('ventas_productos_1.xlxs')
df_archivoExcel = df_archivoExcel[:10].copy()
print(df_archivoExcel)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 11:06:43 2021

@author: ludving
"""


import pandas as pd
import numpy as np
#from scipy import stats

ar_teo = 12.816
dec_teo = 27.4


def aprox_dec1(data):
    data['absDec'] = abs(data['Decl'])
    data.sort_values('absDec', inplace=True, ascending=False)
    data.reset_index(inplace=True)
    data = data.drop([0])
    data.reset_index(inplace=True)
    
    lst1 = data["absDec"].tolist()
    lst2 = data["Decl"].tolist()
    lst3 = data["AR"].tolist()
    
    n = 100
    aproximaciones = []
    declinaciones = []
    ascenciones = []
    for i in range(n):
        #data = data.reset_index()
        aprDec = 90-lst1[i]
        auxDec = round(lst2[i],3)
        auxAR = lst3[i]*15
        aproximaciones.append(aprDec)
        declinaciones.append(auxDec)
        ascenciones.append(auxAR)
        #data = data.drop([i])
    
    aux = list(range(0,n))
    data = data.drop(aux)
    
    
    print('----------------------------')
    print('Valor real de Dec: 27.4')
    print('Promedio de aproximaciones Decl: ',np.mean(aproximaciones))
    print('Mediana de aproximaciones Decl: ',np.median(aproximaciones))
    print('----------------------------')

    rad = [1]*n
    df = pd.DataFrame(list(zip(ascenciones, declinaciones, rad)),columns =['ar', 'dec',"radi"])
    #df.to_csv("DecStars.csv")

data = pd.read_csv('data.csv')
data = data.loc[data['cat'] == 'LUND']
aprox_dec1(data)

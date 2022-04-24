#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:35:28 2021

@author: ludving
"""

def ars_check(ars):
    ars = ars.tolist()
    stat = 1
    flag1 = False
    flag2 = False
    flag1 = all(x < ar_teo for x in ars)
    flag2 = all(x > ar_teo for x in ars)
    if flag1 == True or flag2 == True:
        stat = 0
    return stat
        

def ars_posi(ars):
    ar1 = 0; ar1aux = []
    ar2 = 0; ar2aux = []
    for i in ars:
        if i < ar_teo:
            ar1aux.append(i)
        elif i > ar_teo:
            ar2aux.append(i)
    
    ar1 = np.mean(ar1aux)
    ar2 = np.mean(ar2aux)
    aproxAr = (ar2 - ar1)/2 + ar1
    return aproxAr


def horas_minutos(value):
    horas = int(value)
    minutos =(value - horas)*60
    return(horas, minutos)

def aprox_ar(data):
    
    data['decAprox'] = np.round(data['Decl'],1)
    
    
    
    #ordenamos por la AR y reseteamos los indices
    data.sort_values('decAprox', inplace=True)
    data.reset_index(inplace=True)
    
    ### BUSQUEDA DE PARES
    #for i in range(0,len(data)):
    #    print(data['decAprox'][i])
    
    coincidencia = data.loc[data['decAprox'] == 64.0]
    ars = coincidencia["AR"]
    ar1 = 0; ar1aux = []
    ar2 = 0; ar2aux = []
    for i in ars:
        if i < ar_teo:
            ar1aux.append(i)
        elif i > ar_teo:
            ar2aux.append(i)
    
    ar1 = np.mean(ar1aux)
    ar2 = np.mean(ar2aux)
    aproxAr = (ar2 - ar1)/2 + ar1
    
    aa = data.decAprox.unique()
    arsAprox = []
    arsAproxdeg = []
    for i in aa:
        aproxAr = 0
        coincidencia = data.loc[data['decAprox'] == i]
        ars = coincidencia["AR"]   
        ar1 = 0; ar1aux = []
        ar2 = 0; ar2aux = []
        if len(ars) >= 2:
            flag = ars_check(ars)
            if flag == 1:
                aproxAr = ars_posi(ars)
                #print(flag, aproxAr)
                arsAproxdeg.append(aproxAr*15)
                arsAprox.append(aproxAr)
    promed = np.mean(arsAprox)
    
    
    bestdiff = 100
    for i in arsAprox:
        diff = abs(ar_teo-i)
        if diff<bestdiff:
            mejor_ar = i
            bestdiff = diff
    
    horaproxi, minaproxi = horas_minutos(promed)
    mejorHora, mejorMin = horas_minutos(mejor_ar)
    print('----------------------------')
    print('Valor real de AR: 12 h 49 m')
    print('Mejor AR (con valor teorico): ', mejorHora,'h', round(mejorMin, 1),'m')
    print('Promedio de aproximaciones AR: ',horaproxi,'h', round(minaproxi,1),'m')
    print("Std", np.std(arsAprox))
    print('----------------------------')
    
    arteos = [dec_teo]*len(arsAproxdeg)
    #df = pd.DataFrame(list(zip(arsAproxdeg, arteos)),columns =['ar', 'dec'])

import pandas as pd
import numpy as np
#from scipy import stats

ar_teo = 12.816
dec_teo = 27.4

data = pd.read_csv('data.csv')
#data = data.loc[data['cat'] == 'LUND']
aprox_ar(data)

#df.to_csv("torontoAR.csv")

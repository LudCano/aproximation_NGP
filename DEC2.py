#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:19:57 2021

@author: ludving
"""

def print_res(res):
    decd = int(res)
    decm = (res - decd)*60
    decs = (decm - int(decm))*60
    decm = int(decm)
    
    print(decd,'°', decm, 'm', decs,'°')


### METHOD 2 ON APPROXIMATING THE GALACTIC NORTH POLE (DECLINATION)
# OGLE CATALOGUE


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from scipy import stats

ar_teo = 12.857
dec_teo = 27.4

delta = 0.25
def aprox_dec2(data, delta):
    ran = [ar_teo+delta, ar_teo-delta]
    
    
    
    lst2 = data["AR"].tolist()
    data["ARaprox"] = data["AR"].round(2)
    
    #stars = data.loc[data['ARaprox'] == 12]
    stars = data.loc[data['AR'].between(ran[1], ran[0], inclusive=True)]
    #stars = data.loc[data['ARaprox'] == 12.85]
    #stars = data.loc[data['ARaprox'] > 12.318 and data['ARaprox'] < 13.318]
    lst1 = stars["Decl"].tolist()
    lst2 = stars["AR2"].tolist()
    
    
    aprox = []
    for i in lst1:
        aux = 90 - abs(i)
        aprox.append(aux)
        
    res = np.mean(aprox) 
    print(np.mean(aprox))
    #plt.plot(aprox)
    print_res(res)
    print_res(dec_teo)

    rad = [1]*len(aprox)
    df = pd.DataFrame(list(zip(lst1, lst2, rad)),columns =['dec', 'ar',"radi"])
    #df.to_csv("DecStars2.csv")
data = pd.read_csv('data.csv')
data = data.loc[data['cat'] == 'LUND']
aprox_dec2(data, delta)
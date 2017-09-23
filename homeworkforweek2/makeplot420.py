#! /usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import xlrd
from astropy.io import fits

data20 = xlrd.open_workbook('C:/Users/chaowang/20mstars.xlsx')  #read data
sheet=data20.sheets()[0]
col1=sheet.col_values(0)
col2=sheet.col_values(1)
col3=sheet.col_values(2)

M53 = fits.open('M53-1000.fit')  #load fits
rawdata=M53[1].data
L=[i for i in range(23535)]
T=[i for i in range(23535)]
for i in np.arange(0,23535,1):
    L[i]=rawdata[i][3]-16.5
    T[i]=rawdata[i][4]

for i in range(20):
    plt.annotate(col3[i], xy=(col2[i], col1[i]), xytext=(col2[i]+0.2, col1[i]-0.2),color="black",arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))


plt.xlabel('<-------------------------------B-V(Mag)')
plt.ylabel('Luminosity(ABS Mag) ------------------------------>')
plt.title('HR for 20 stars diagram')
plt.gca().invert_yaxis()
plt.scatter(T,L,s=2,color="blue")
plt.scatter(col2,col1,s=100,color="red")#color="black"


plt.savefig('result20.png')
plt.show()



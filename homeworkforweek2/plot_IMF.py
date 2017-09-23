import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from itertools import groupby

asu = fits.open('asu.fit')  #load fits
rawdata=asu[1].data
Mag=[i for i in range(len(rawdata))]
mag=[i-22 for i in range(40)]
for i in range(len(rawdata)):
    Mag[i]=rawdata[i][1]-10+5*(np.log(abs(rawdata[i][2])))/(np.log(10))
for b in Mag:
    if (b >13.5) or (b <-4.5):
        Mag.remove(b)
for k, g in groupby(sorted(Mag), key=lambda x:x//1):
    if k > -5:
        mag[int(k+22)]=len(list(g))
VMagnumber=mag[18:36]
x=[i-4 for i in range(18)]



plt.xlabel('Luminosity(VMag)')
plt.ylabel('Number')
plt.yscale('log')
plt.title('LN diagram')
plt.plot(x,VMagnumber)
plt.savefig('imf-NL(m).png')
plt.show()

x2=[ 10**(((i-4)*(-3)/17+1.3)) for i in range(18)]
plt.xscale('log')
plt.yscale('log')
plt.ylabel('Number')
plt.xlabel('Mass(M/Msun)')
plt.title('MN diagram')
plt.plot(x2,VMagnumber)
plt.savefig('imf-NM.png')
plt.show()

y=[0 for i in range(18)]
for i in range(18):
    y[i]=VMagnumber[i]/(x2[i])**(2.5)
plt.xscale('log')
plt.yscale('log')
plt.ylabel('Number per')
plt.xlabel('Mass(M/Msun)')
plt.title('IMF diagram')
plt.plot(x2,y)
plt.savefig('imf.png')
plt.show()


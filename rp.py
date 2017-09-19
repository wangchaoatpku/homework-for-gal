# Make external packages available
from astropy.io import ascii
import matplotlib.pyplot as plt
import numpy as np

# Read table.
# ==> dat[column_name] and dat[row_number] both valid <==
data_url = 'https://raw.githubusercontent.com/python4astronomers/python4astronomers/stable/examples/tables/fermi_agn.dat'
dat = ascii.read(data_url)

redshift = dat['redshift']    # array of values from 'redshift' column
flux = dat['photon_flux']
gamma = dat['spectral_index']

# Select rows that have a measured redshift
with_z = (redshift != -999)

plt.figure(1)
plt.semilogx(flux, gamma, '.b', label='All')  # First plot!
plt.semilogx(flux[with_z], gamma[with_z], 'or', label='With Z')
plt.legend(numpoints=1)
plt.grid()
plt.xlabel('Flux (photon/cm$^2$/s)')   # latex works
plt.ylabel('Spectral index $\Gamma$')
plt.show()



# Select low- and high-z samples
lowz = with_z & (redshift < 0.8)
highz = with_z & (redshift >= 0.8)

plt.figure(2)
bins = np.arange(1.2, 3.0, 0.1)    # values from 1.2 to 3.0 by 0.1
plt.hist(gamma[lowz], bins, color='b', alpha=0.5, label='z < 0.8')
plt.hist(gamma[highz], bins, color='r', alpha=0.5, label='z > 0.8')
plt.xlabel('Spectral index $\Gamma$')
plt.title('$\Gamma$ for low-z and high-z samples')
plt.legend(loc='upper left')
plt.show()
ascii.write(dat[with_z], 'fermi_agn_with_z.dat')
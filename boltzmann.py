## Joseph Godoy -- Boltzmann.py ##

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

m  = .0280134 / (6.022 * 10**23) #Nitrogen Mass (Kg)
k  = 1.38064852E-23 # Boltzmann's Constant (Joules/Kelvin)
T  = 300 #Kelvin
v1 = 399 #m/s
v2 = 401 #m/s


def boltzmann(v):
    return (4.0/(np.sqrt(np.pi))) * (1.0 / (np.sqrt(2*k*T / m))**3) * v**2 * np.exp(-v**2/(np.sqrt(2.0*k*T / m))**2)
probability, err = quad(boltzmann, v1, v2)

print(probability)

v_array = np.linspace(0, 1000, 100) # v_array is a 100 element array from 0.0 to 1000.0.

#print(len(v_array))
#print(v_array[0], v_array[-1])

plt.plot(v_array,boltzmann(v_array))
plt.show()

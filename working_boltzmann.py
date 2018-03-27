## Joseph Godoy -- Boltzmann.py ##

import numpy as np
from scipy.integrate import quad

# Constants

m  = .0280134 / (6.022 * 10**23) #check the mass
k  = 1.38064852E-23
T  = 300
v1 = 399
v2 = 401


def boltzmann(v):
    return (4.0/(np.sqrt(np.pi))) * (1.0 / (np.sqrt(2*k*T / m))**3) * v**2 * np.exp(-v**2/(np.sqrt(2.0*k*T / m))**2)
probability, err = quad(boltzmann, v1, v2)

print(probability)
print(err)

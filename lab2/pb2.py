# Generati un semnal sinusoidal de amplitudine unitară si frecventă aleasă
# de voi. Încercati 4 valori diferite pentru fază. Afisati toate semnalele pe
# acelasi grafic. Adăugati zgmot aleator sinusoidelor esantionate generate.
# Noul semnal este x[n] + γz[n] astfel ı̂ncât raportul semnal zgomot (Signal
# to Noise Ratio sau SNR) să fie {0.1, 1, 10, 100}.
import numpy as np
import matplotlib.pyplot as plt
import math

def find_gamma(sin, z, snr):
    sin_l2 = np.linalg.norm(sin)
    z_l2 = np.linalg.norm(z)
    return math.sqrt((sin_l2 ** 2)/(z_l2 ** 2 * snr))

num_samples = 1000
freq = 300 # Hz
A = 1
phi1 = np.pi/3
phi2 = np.pi
phi3 = np.pi/6
phi4 = np.pi/4

t = np.linspace(0, 0.01, num_samples)
fig, axs = plt.subplots(2, 4, figsize=(15, 5))

z = np.random.normal(0, 1, num_samples)

sin1 = A*np.sin(2*np.pi*freq*t + phi1)
sin2 = A*np.sin(2*np.pi*freq*t + phi2)
sin3 = A*np.sin(2*np.pi*freq*t + phi3)
sin4 = A*np.sin(2*np.pi*freq*t + phi4)

axs[0, 0].plot(t, sin1)
axs[0, 0].set_title('Plot of sin with phi = pi/3')

axs[0, 1].plot(t, sin2)
axs[0, 1].set_title('Plot of sin with phi = pi')

axs[0, 2].plot(t, sin3)
axs[0, 2].set_title('Plot of sin with phi = pi/6')

axs[0, 3].plot(t, sin4)
axs[0, 3].set_title('Plot of sin with phi = pi/4')

gamma1 = find_gamma(sin1, z, 0.1)
gamma2 = find_gamma(sin2, z, 1)
gamma3 = find_gamma(sin3, z, 10)
gamma4 = find_gamma(sin4, z, 100)

sign1 = sin1 + z*gamma1
sign2 = sin2 + z*gamma2
sign3 = sin3 + z*gamma3
sign4 = sin4 + z*gamma4

axs[1, 0].plot(t, sign1)
axs[1, 0].set_title('Plot of sin with phi = pi/3 with noise')

axs[1, 1].plot(t, sign2)
axs[1, 1].set_title('Plot of sin with phi = pi with noise')

axs[1, 2].plot(t, sign3)
axs[1, 2].set_title('Plot of sin with phi = pi/6 with noise')

axs[1, 3].plot(t, sign4)
axs[1, 3].set_title('Plot of sin with phi = pi/4 with noise')

plt.tight_layout()
plt.show()
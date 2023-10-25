# 4. Generati doua semnale cu forme de unda diferite (ex. unul sinusoidal,
# celalalt sawtooth) si adunati-le esantioanele. Afisati grafic cele doua semnale initiale si 
# suma lor, fiecare in cate un subplot.

import numpy as np
import matplotlib.pyplot as plt

# semnal sawtooth cu freq = 800Hz
freq1 = 800 # Hz
t1 = np.arange(0, 10*freq1, 1)
res1 = np.mod(t1, 10)

# semnal sinusoidal cu freq = 330Hz
freq2 = 330 # Hz
t2 = np.linspace(0, 1, 10*freq1)
res2 = np.sin(freq2 * 2 * np.pi * t2)

# suma semnalelor (res1 + res2)
res3 = res1 + res2

fig, ax = plt.subplots(nrows=3)
ax[0].plot(t2[:100], res1[:100])
ax[1].plot(t2[:100], res2[:100])
ax[2].plot(t2[:100], res3[:100])
plt.show()
# 7. Generati un semnal sinusoidal de frecventa 1000 Hz si decimati-l la 1/4
# din frecventa initiala (pastrati doar al 4-lea fiecare element din vector).
# (a) Afisati grafic cele doua semnale si comentati diferentele.
# (b) Repetati decimarea (tot la 1/4 din frecventa initiala) pornind acum
# de la al doilea element din vector. Ce observati? Este decimarea
# invarianta in timp?

import numpy as np
import matplotlib.pyplot as plt

freq = 1000
num_samples = 10000

# semnalul initial
t = np.linspace(0, 1, num_samples)
s = np.sin(2*np.pi * freq * t)

# (a) - semnalele difera, desi au fost esantionate din acelasi semnal, 
# esantioanele au fost alese la momente diferite de timp si frecventa 
# de esantionare a semnalului decimat este mult mai mica decat frecventa 
# sinusoidei, deci nu poate fi reconstruit semnalul corespunzator
s1 = [elem for i, elem in enumerate(s) if i % 4 == 0]

# (b) - decimarea nu este invarianta in timp
s2 = [elem for i, elem in enumerate(s) if i % 4 == 1]
new_t = np.linspace(0, 1, np.shape(s1)[0])

# plotare
fig, ax = plt.subplots(nrows=3)
ax[0].plot(t[:60], s[:60])
ax[1].plot(new_t[:15], s1[:15])
ax[2].plot(new_t[:15], s2[:15])

plt.show()
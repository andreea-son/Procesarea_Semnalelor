# 6. Generati 3 semnale de tip sinus cu amplitudine unitara si faza nula avand
# frecventele fundamentale:
# (a) f = fs/2
# (b) f = fs/4
# (c) f = 0 Hz
# unde fs este frecventa de esantionare, aleasa de voi. Notati ce observati.

import numpy as np
import matplotlib.pyplot as plt

fs = 2000

t = np.linspace(0, 1, 2000)
# (a) f = fs/2
s1 = np.sin(2*np.pi * fs/2 * t)
# (b) f = fs/4
s2 = np.sin(2*np.pi * fs/4 * t)
# (c) f = 0 Hz
s3 = np.sin(2*np.pi * 0 * t)

fig, ax = plt.subplots(nrows=3)

ax[0].plot(t[:100], s1[:100])
ax[1].plot(t[:100], s2[:100])
ax[2].plot(t[:100], s3[:100])
plt.show()

# se observa: amplitudinea primei sinusoide pare ca se modifica in timp (creste), 
# in timp ce cea de a doua sinusoida este redata corect, iar ultimul plot, 
# avand frecventa 0 Hz este o simpla dreapta (sin(0) = 0)
import numpy as np
import matplotlib.pyplot as plt

# Generati un semnal sinusoidal de tip sinus, de amplitudine, frecventă si
# fază aleasă de voi. Generati apoi un semnal de tip cosinus astfel ı̂ncât pe
# orizontul de timp ales, acesta să fie identic cu semnalul sinus. Verificati
# afisându-le grafic ı̂n două subplot-uri diferite.
num_samples = 1000
freq = 200 # Hz
A = 2
phi = np.pi/3
delta = np.pi/2

t = np.linspace(0, 0.01, num_samples)
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

sin = A*np.sin(2*np.pi*freq*t + phi)
cos = A*np.cos(2*np.pi*freq*t + phi - delta)

axs[0].plot(t, sin)
axs[0].set_title('Plot of sin')

axs[1].plot(t, cos)
axs[1].set_title('Plot of cos')

plt.tight_layout()
plt.show()

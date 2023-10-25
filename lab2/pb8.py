# 8. In practica se opereaza des cu urmatoarea aproximare: pentru valori mici
# ale lui x, sin(x) = x. Verificati daca aceasta aproximare este corecta,
# reprezentand grafic cele doua curbe pentru valori ale lui x in intervalul
# [-pi/2, pi/2]. Arătati si un grafic cu eroarea dintre cele două functii.
# Folositi si aproximarea Pade, nu doar Taylor.

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi/2, np.pi/2, 2000)
sin_x = np.sin(t)
aprox_taylor = t
aprox_pade = (t - (7 * t**3)/60)/(1 + (t**2)/20)
err1 = np.abs(sin_x - aprox_taylor)
err2 = np.abs(sin_x - aprox_pade)

plt.plot(t, sin_x, label='sin(x)', color='green')
plt.plot(t, aprox_taylor, label='aprox_taylor', color='blue')
plt.plot(t, aprox_pade, label='aprox_pade', color='red')
plt.title('Comparare curbe')
plt.legend()
plt.show()

plt.plot(t, err1, label='eroare_taylor')
plt.title('Eroarea dintre sin(x) si aprox_taylor')
plt.legend()
plt.show()

plt.plot(t, err2, label='eroare_pade')
plt.title('Eroarea dintre sin(x) si aprox_pade')
plt.legend()
plt.show()

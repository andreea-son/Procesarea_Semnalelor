import matplotlib.pyplot as plt
import numpy as np
import math

def my_sine(t, freq, a):
    return a*np.sin(2*np.pi*freq*t)

def fourier(func, freq):
    N = len(func)
    my_list = []
    for n in range(N):
        my_list.append(func[n] * math.e**((-2*np.pi*1j * freq * n) / N))
    return np.array(my_list)

def dft_magnitude(F_omega):
    return abs(np.sum(F_omega))

t = np.linspace(0, 1, 2000)
freqs = [5, 20, 35, 50, 65, 80]
a = [1.5, 0.75, 1.5, 1, 2, 0.5]
func = np.zeros(2000)
for i in range(len(freqs)):
    func += my_sine(t, freqs[i], a[i])

magnitudes = []
for freq in range(100):
    F_omega = fourier(func, freq)
    magnitudes.append(dft_magnitude(F_omega)/1000)

magnitude_t = []
for i in range(100):
    magnitude_t.append(i+1)

fig, axis = plt.subplots(1,2)

axis[0].plot(t, func)
axis[1].plot(magnitude_t, magnitudes)

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Un semnal sinusoidal de frecventa 400 Hz, care sa contina 1600 de
# esantioane.
num_samples = 1600
freq = 400 # Hz
t = np.linspace(0, 0.01, num_samples)
res1 = np.sin(2*np.pi*freq*t)
plt.plot(t, res1)
plt.title("sin cu freq = 400 Hz si num_esantione = 1600")
plt.show()

# Un semnal sinusoidal de frecventa 800 Hz, care sa dureze 3 secunde
num_samples = 100000
freq = 800 # Hz
t = np.linspace(0, 3, num_samples)
res2 = np.sin(2*np.pi*freq*t)
# Daca semnalul ar dura 3 secunde, atunci am avea 2400 de repetitii ale sinusoidei, ceea ce nu poate fi vizualizat
# plotez doar o bucata din semnal
plt.plot(t[:500], res2[:500])
plt.title("sin cu freq = 800 Hz si interval_timp = 3s")
plt.show()

# Un semnal de tip sawtooth de frecventa 240 Hz
freq = 240 # Hz
modulo = 10
t = np.linspace(0, 1, modulo*freq)
res3 = np.arange(0, modulo*freq, 1)
res3 = np.mod(res3, modulo)
plt.plot(t[:51], res3[:51])   
plt.title("sawtooth cu freq = 240 Hz")
plt.show()

# Un semnal de tip square de frecventa 300 Hz
freq = 300 # Hz
modulo = 100
t = np.linspace(0, 1, freq*modulo)
res4 = [0 if i % modulo < 50 else 1 for i in range(len(t))]
plt.plot(t[:500], res4[:500])
plt.title("square wave cu freq = 300 Hz")
plt.show()

# # square wave ca suma de sinusoide
# t = np.linspace(0, 1, 10000)
# res4 = np.zeros(10000)
# for i in range(len(t)):
#     for j in range(50):
#         res4[i] += np.sin((2*j+1)*np.pi*t[i])/(2*j+1)
# plt.plot(t, res4)
# print(res4[:50])
# plt.title("square wave cu freq = 300 Hz")
# plt.show()

# Un semnal 2D aleator. Creati un numpy.array de dimensiune 128x128
# si initializati-l aleator, folosind numpy.random.rand(x,y), unde x si
# y reprezinta numarul de linii respectiv de coloane. Afisatii semnalul
# generat folosind functia imshow(I) din matplotlib.
img1 = np.random.rand(128, 128)
plt.imshow(img1)
plt.title("Imagine 128 x 128 initializata random")
plt.show()

# Un semnal 2D la alegerea voastra. Creati un numpy.array de dimensiune 128x128 si initializati-l folosind o procedura 
# creata de voi. Utilizati, spre exemplu, functiile numpy.zeros() si numpy.ones().
def func(x, y):
    return 3 * np.sin(x + y) + np.cos(x + 3 * y)

img2 = np.zeros((128, 128))
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
       img2[i][j] = np.abs(func(i, j))
plt.imshow(img2)
plt.title("Imagine 128 x 128 initializata printr-o functie")
plt.show()
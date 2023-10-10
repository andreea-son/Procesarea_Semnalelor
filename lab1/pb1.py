import numpy as np
import matplotlib.pyplot as plt

# simulati axa reala 
t = np.arange(0, 0.03, 0.0005)

# construiti semnalele
signal1_t = np.cos(520*np.pi*t + np.pi/3)
signal2_t = np.cos(280*np.pi*t - np.pi/3)
signal3_t = np.cos(120*np.pi*t + np.pi/3)

# afisati grafic semnalele in cate un subplot
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].plot(t, signal1_t)
axs[0].set_title('Plot of x')

axs[1].plot(t, signal2_t)
axs[1].set_title('Plot of y')

axs[2].plot(t, signal3_t)
axs[2].set_title('Plot of z')

plt.tight_layout()
plt.show()

freq = 200 # Hz
time_interval = 0.03
n = np.linspace(0, 0.03, int(freq * time_interval))

# esantionati semnalele cu o frecventa de 200Hz
signal1_n = np.cos(520*np.pi*n + np.pi/3)
signal2_n = np.cos(280*np.pi*n - np.pi/3)
signal3_n = np.cos(120*np.pi*n + np.pi/3)

# afisati grafic semnalele esantionate, in cate un subplot
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].stem(n, signal1_n)
axs[0].set_title('Plot of x')

axs[1].stem(n, signal2_n)
axs[1].set_title('Plot of y')

axs[2].stem(n, signal3_n)
axs[2].set_title('Plot of z')

plt.tight_layout()
plt.show()

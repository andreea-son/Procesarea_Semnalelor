# 3. Ascultati semnalele pe care le-ati generat la laboratorul precedent pentru exercitiile 2.(a)-(d)
# folosind biblioteca sounddevice. Salvati unul din semnale ca fisier .wav si verificati ca il puteti
# incarca de pe disc utilizand scipy.io.wavfile.read().

import scipy.io.wavfile
import scipy.signal
import sounddevice
import time
import numpy as np

# Un semnal sinusoidal de frecventa 400 Hz, care sa contina 1600 de
# esantioane.
num_samples = 44100 # am modifical num_samples = sf (=44100)
freq = 400 # Hz
t = np.linspace(0, 1, num_samples)
res1 = np.sin(2*np.pi*freq*t)

# Un semnal sinusoidal de frecventa 800 Hz, care sa dureze 3 secunde
num_samples = 44100*3
freq = 800 # Hz
t = np.linspace(0, 3, num_samples)
res2 = np.sin(2*np.pi*freq*t)

# Un semnal de tip sawtooth de frecventa 240 Hz
num_samples = 44100
t = np.linspace(0, 1, num_samples)
freq = 240
res3 = np.mod(t * freq, 1) * 2 - 1

# Un semnal de tip square de frecventa 300 Hz
t = np.linspace(0, 1, 44100)
res4 = np.zeros(44100)

freq = 300
count = 44100 / freq / 2
curr_val = 0
for i in range(1, 44101):
    if i % count == 0:
        curr_val = not(curr_val)
    res4[i-1] = curr_val

res4 = np.array(res4)
semnale = [res1, res2, res3, res4]

sf = 44100 # sample freq
filenames = []
for i, semnal in enumerate(semnale):
    filename = "semnal-%d.wav" % (i)
    scipy.io.wavfile.write(filename, sf, semnal)
    filenames.append(filename)

for filename in filenames:
    print(filename)
    samplerate, signal = scipy.io.wavfile.read(filename)
    sounddevice.play(signal, samplerate)
    time.sleep(2)

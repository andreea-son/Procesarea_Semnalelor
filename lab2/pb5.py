# 5. Generati doua semnale cu aceeasi forma de unda, dar de frecvente diferite,
# si puneti-le unul dupa celalalt in acelasi vector. Redati audio rezultatul si
# notati ce observati

import scipy.io.wavfile
import scipy.signal
import sounddevice
import numpy as np

sf = 44100
t = np.linspace(0, 1, sf)

s1 = np.cos(300 * 2*np.pi * t)
s2 = np.cos(500 * 2*np.pi * t)

s_final = np.concatenate((s1, s2), axis=0)

sounddevice.play(s_final, sf)
scipy.io.wavfile.write('semnal_pb5.wav', sf, s_final)

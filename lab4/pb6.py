from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

samplerate, data = wavfile.read("vocale.wav")

N = len(data)
group_size = int(N * 0.01)
overlap_size = int(group_size * 0.5)
groups = [data[i:i+group_size] for i in range(0, N-group_size+1, overlap_size)]

fft_matrix = np.zeros((len(groups), len(groups[0])))
for i, group in enumerate(groups):
    group_fft = np.fft.fft(group)
    fft_matrix[i, :] = np.abs(group_fft)

plt.imshow(fft_matrix)
plt.show()

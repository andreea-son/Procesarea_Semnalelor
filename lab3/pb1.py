import numpy as np
import matplotlib.pyplot as plt
import math

matrix = np.zeros((8, 8), dtype=np.complex_)
for m in range(matrix.shape[0]):
    for n in range(matrix.shape[1]):
        matrix[m][n] = math.e**((2*math.pi*1j*m*n)/8)

t = np.arange(0, 8)

fig, axs = plt.subplots(1, 8, figsize=(20, 5))

for i in range(matrix.shape[0]):
    v = matrix[i][:]
    my_cos = np.real(v)
    my_sin = np.imag(v)
    axs[i].plot(t, my_cos)
    axs[i].plot(t, my_sin)
    plt.tight_layout()

plt.show()

conj_matrix = matrix.conj().T

if np.linalg.norm(abs(conj_matrix * matrix) - 8 * np.identity(8) < 10e-10):
    print("adevarat")
else:
    print("fals")
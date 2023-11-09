import cmath
import numpy as np
import time
import matplotlib.pyplot as plt

def my_fourier(x):
    N = len(x)
    X = np.zeros(N, dtype=np.complex_)
    
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * cmath.exp(-2j * np.pi * k * n / N)
    
    return X


def main():
    N = [2**(7+i) for i in range(7)]
    freq = 10
    my_fourier_times = []
    np_fourier_times = []
    for n in N:
        t = np.linspace(0, 1, n)
        y = np.sin(2*np.pi*t*freq)
        start = time.time()
        F = np.fft.fft(y)
        duration = time.time() - start
        print(duration)
        np_fourier_times.append(duration)
        start = time.time()
        F = my_fourier(y)
        duration = time.time() - start
        print(duration)
        my_fourier_times.append(duration)
        print("==")

    t = np.linspace(0, 7, 7)
    plt.plot(t, my_fourier_times, scaley='log', label='my_fourier_times')
    plt.plot(t, np_fourier_times, scaley='log', label='np_fourier_times')
    plt.legend()
    plt.show()
main()
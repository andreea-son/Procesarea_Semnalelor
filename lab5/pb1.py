# 1) 
# a) semnalul este esantionat din ora in ora => freq = 1/3600 Hz
# b) fiind 18288 esantionane din ora in ora, intervalul
# de timp acoperit este de 18288 h
# c) frecventa maxima prezenta in semnal este de 1/1800 = 0.000(5) Hz

# d)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def punctul_d(fileName='Train.csv'):
    fs = 1/3600
    df = pd.read_csv(fileName)
    x = np.asarray(df.iloc[:, 2])
    N = len(x)
    length = int(N/2)
    X = np.fft.fft(x)
    X = abs(X)/N
    X = X[:length]
    f = fs * np.linspace(0, length, length) / N
    plt.plot(f, X)
    plt.show()
    
    return X, x, f

# e)
def punctul_e(X, f):
    X = X[15:]
    f = f[15:]
    return X, f

# f)
def punctul_f(X, f):
    idx = np.argpartition(X, -4)[-4:]
    ampl = X[idx]
    freq = f[idx]
    for i in range(4):
        print(f"{ampl[i]} {freq[i]}\n")

# g)
def punctul_g(X, fileName='Train.csv'):
    df = pd.read_csv(fileName)
    dates = np.asarray(df.iloc[:, 1], dtype=object)
    for idx, date_str in enumerate(dates):
        date_format = '%d-%m-%Y %H:%M'
        date_obj = datetime.strptime(date_str, date_format)
        if date_obj.weekday() == 0:
            index_monday = idx
            break
    one_month = 24*7*31
    nsamples = one_month
    X = X[index_monday:(index_monday+nsamples)]
    t = np.arange(0, nsamples, 1)
    plt.plot(t, X)
    plt.show()

# h)
# putem presupune ca zilele de sambata si duminica au un trafic mult mai redus fata de ziua de luni si, plotand primele saptamani,
# putem incerca sa intuim (in functie de cum arata graficul) zilele de duminica, aflate imediat inaintea celor de luni. 

# def punctul_i(x):
#     fs = 1/3600
#     N = len(x)
#     X = np.fft.fft(x)
#     X_init = X.copy()
#     t = fs * np.linspace(0, N, N)
#     freqs_init = np.fft.fftfreq(N, 1/fs)

#     min_idx = np.argmin(freqs_init)
#     min_freq = freqs_init[min_idx]

#     tenth_largest_idx = np.argsort(freqs_init)[-10]
#     tenth_largest_freq = freqs_init[tenth_largest_idx]

#     print(min_freq)
#     print(tenth_largest_freq)
    
#     X[(freqs_init>tenth_largest_freq)] = 0

#     freqs_final = np.fft.fftfreq(len(X), 1/fs)

#     filtered_signal = np.fft.ifft(X)

#     fig, axis = plt.subplots(2, 2)
    
#     axis[0][0].plot(t, freqs_init)
#     axis[0][1].plot(t, freqs_final)

#     axis[1][0].plot(t, x)
#     axis[1][1].plot(t, filtered_signal)
    
#     plt.tight_layout()
#     plt.show()


X, x, f = punctul_d()
X, f = punctul_e(X, f)
punctul_f(X, f)
punctul_g(X)
# punctul_i(x)
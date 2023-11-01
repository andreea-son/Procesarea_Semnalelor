import matplotlib.pyplot as plt
import numpy as np
import math

def sine_func(t, freq, a=1):
    return a*np.sin(2*np.pi*freq*t)

def fourier(func, freq):
    N = len(func)
    my_list = []
    for n in range(N):
        my_list.append(func[n] * math.e**((-2*np.pi*1j * freq * n) / N))
    return np.array(my_list)

def fig1(sine_func):
    freq = 1
    pos = 500
    res = fourier(sine_func, freq)
    first_line_x = [pos, pos]
    first_line_y = [0, sine_func[pos]]
    second_line_x = [0, res[pos].real]
    second_line_y = [0, res[pos].imag]

    _, axis = plt.subplots(1, 2)
    
    axis[0].plot(sine_func)
    axis[0].plot(first_line_x, first_line_y, color='green')
    axis[0].plot(pos, sine_func[pos], marker='o', color='green')
    
    axis[1].plot(res.real, res.imag)
    axis[1].plot(res[pos].real, res[pos].imag, marker='o', color='green')
    axis[1].plot(second_line_x, second_line_y, color='green')
    
    plt.tight_layout()
    plt.show()
    
def fig2(sine_func):
    res = []
    wrapping_freqs = [2, 4, 3, 7]
    for crt_freq in wrapping_freqs:
        res.append(fourier(sine_func, crt_freq))
    
    _, axis = plt.subplots(2, 2)

    axis[0,0].plot(res[0].real, res[0].imag)
    axis[0,0].set_title('ω = 2')

    axis[0,1].plot(res[1].real, res[1].imag)
    axis[0,1].set_title('ω = 4')

    axis[1,0].plot(res[2].real, res[2].imag)
    axis[1,0].set_title('ω = 3')

    axis[1,1].plot(res[3].real, res[3].imag)
    axis[1,1].set_title('ω = 7')
    
    plt.tight_layout()
    plt.show()
    
t = np.linspace(0, 1, 2000)
freq = 7
sine = sine_func(t, freq)

fig1(sine)
fig2(sine)

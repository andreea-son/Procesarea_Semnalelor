import numpy as np
import matplotlib.pyplot as plt

def my_sine(t, freq=1, amplitude=1):
    return amplitude*np.sin(2*np.pi*freq*t)

def main():
    f0 = 3
    f_s = 5
    k1 = 1
    k2 = 2
    f1 = f0 + k1*f_s
    f2 = f0 + k2*f_s

    length = 2500
    t = np.linspace(0, 1, length)
    sin1 = my_sine(t, f0)
    sin2 = my_sine(t, f1)
    sin3 = my_sine(t, f2)

    my_t = []
    my_arr = []
    num_samples = f_s
    for i in range(num_samples+1):
        index = int(i*length/num_samples)
        if index == length:
            index -= 1
        my_t.append(t[index])
        my_arr.append(sin1[index])

    fig, axis = plt.subplots(4, 1)

    axis[0].plot(t, sin1)
    
    axis[1].plot(t, sin1)
    axis[1].stem(my_t, my_arr, markerfmt='ro')

    axis[2].plot(t, sin2)
    axis[2].stem(my_t, my_arr, markerfmt='ro')

    axis[3].plot(t, sin3)
    axis[3].stem(my_t, my_arr, markerfmt='ro')

    plt.tight_layout()
    plt.show()
main()
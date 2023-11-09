import numpy as np
import matplotlib.pyplot as plt

def my_sine(t, freq=1, amplitude=1):
    return amplitude*np.sin(2*np.pi*freq*t)

def main():
    f_s = 31
    # acum, putem construi semnale cu frecv <= 15 si nu va avea loc nicio confuzie
    f0 = 3
    f1 = 8
    f2 = 11

    length = 2500
    t = np.linspace(0, 1, length)
    sin1 = my_sine(t, f0)
    sin2 = my_sine(t, f1)
    sin3 = my_sine(t, f2)

    my_t = []
    my_arr1 = []
    my_arr2 = []
    my_arr3 = []
    num_samples = f_s
    for i in range(num_samples+1):
        index = int(i*length/num_samples)
        if index == length:
            index -= 1
        my_t.append(t[index])
        my_arr1.append(sin1[index])
        my_arr2.append(sin2[index])
        my_arr3.append(sin3[index])

    fig, axis = plt.subplots(4, 1)

    axis[0].plot(t, sin1)
    
    axis[1].plot(t, sin1)
    axis[1].stem(my_t, my_arr1, markerfmt='ro')
    axis[1].plot(my_t, my_arr1)

    axis[2].plot(t, sin2)
    axis[2].stem(my_t, my_arr2, markerfmt='ro')
    axis[2].plot(my_t, my_arr2)

    axis[3].plot(t, sin3)
    axis[3].stem(my_t, my_arr3, markerfmt='ro')
    axis[3].plot(my_t, my_arr3)

    plt.tight_layout()
    plt.show()
main()
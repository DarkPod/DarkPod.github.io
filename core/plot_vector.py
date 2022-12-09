import os
import time
from datetime import datetime

import cv2
import matplotlib.colors as clr
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from cycler import cycler

PRIMES = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
]


def generate_zeta_vector(ord, pow):
    zeta = 1 / (ord**pow)
    realpart = np.real(zeta)
    imagpart = np.imag(zeta)
    vect = np.array([realpart, imagpart])
    return vect


if __name__ == "__main__":

    # V = np.array([[1, 1], [-2, 2], [4, -7]])
    # origin = np.array([[0, 0, 0], [0, 0, 0]])  # origin point
    # plt.quiver(*origin, V[:, 0], V[:, 1], color=["r", "b", "g"], scale=21)
    # plt.show()
    # a = 0

    pace = 0.1
    # Colors
    cmap = plt.cm.gist_rainbow
    pace = 0.01
    r_x = 0.1
    r_y = 0.1
    prod = np.ones(len(range(-int(r_y / pace), int(r_y / pace))) * len(range(-int(r_x / pace), int(r_x / pace))) - 1)

    offset_real = 0
    offset_imag = 0
    for prime in PRIMES:
        s = []
        x = []
        y = []
        for real in range(-int(r_x / pace), int(r_x / pace)):
            real = real * pace + offset_real
            for imag in range(-int(r_y / pace), int(r_y / pace)):
                imag = imag * pace + offset_imag
                if real == 0:
                    damn = 1
                if (real == 0) & (imag == 0):
                    continue
                n = 1 / (1 - prime ** (-((real + imag * 1j) ** (-1))))
                s.append(n)
                x.append(real)
                y.append(imag)
        term = np.array(s)
        prod = prod * term
        # prod = term
        # prod = np.real(term)
        plt.close()
        fig = plt.figure(figsize=(10, 10))
        prod_plot = prod
        x = np.array(x)
        y = np.array(y)
        sr = np.real(prod_plot)
        si = np.imag(prod_plot)
        sr = sr / np.sqrt((sr**2 + si**2))
        si = si / np.sqrt((np.real(prod_plot) ** 2 + si**2))
        plt.quiver(
            x,
            y,
            sr,
            si,
            # label=""
        )
        # legend = plt.legend(loc="upper left", shadow=True, fontsize="medium")
        # plt.axis("auto")
        # plt.plot([-1, 1], [14.13, 14.13])
        plt.title(f"'Zeta' with P = {prime}")
        plt.xlabel("Re", family="serif", color="r", weight="normal", size=16, labelpad=6)
        plt.ylabel("Im", family="serif", color="r", weight="normal", size=16, labelpad=6)
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        os.makedirs("log", exist_ok=True)
        plt.savefig("log/" + timestamp + ".png")
        time.sleep(0.5)
        # plt.show()

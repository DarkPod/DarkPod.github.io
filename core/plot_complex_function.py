import os
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


def generate_random_vector():
    return np.random.rand(2)


def generate_zeta_vector(ord, pow):
    zeta = 1 / (ord**pow)
    realpart = np.real(zeta)
    imagpart = np.imag(zeta)
    vect = np.array([realpart, imagpart])
    return vect


if __name__ == "__main__":

    pace = 0.1
    # Colors
    # get colormap
    cmap = plt.cm.gist_rainbow
    # build cycler with 5 equally spaced colors from that colormap
    # c = cycler("color", cmap(np.linspace(0, 1, n_order)))
    # supply cycler to the rcParam
    # plt.rcParams["axes.prop_cycle"] = c
    pace = 0.1
    r_x = 4
    r_y = 8
    prod = np.ones(len(range(-int(r_y / pace), int(r_y / pace))) * len(range(-int(r_x / pace), int(r_x / pace))))
    offset_imag = 9
    offset_real = 3
    for prime in PRIMES:
        s = []
        x = []
        y = []
        # mod = []
        for real in range(-int(r_x / pace), int(r_x / pace)):
            real = real * pace + offset_real
            for imag in range(-int(r_y / pace), int(r_y / pace)):
                imag = imag * pace + offset_imag
                if real == 0:
                    damn = 1
                if (real == 0) & (imag == 0):
                    continue
                # n = 1 / (1 - prime ** (-(real + imag * 1j)))
                n = 1 / (real + imag * 1j)
                s.append(n)
                x.append(real)
                y.append(imag)
                # mod.append(np.real(n)**2+np.imag(n)**2)
        term = np.array(s)
        # term = np.log(term)
        prod = prod * term
        # prod = np.imag(prod)
        # prod = np.real(prod) ** 2 + np.imag(prod) ** 2
        prod = np.real(term)

        fig = plt.figure(figsize=(10, 10))
        # ax = plt.axes(projection="3d")
        # ax.scatter3D(X, Y, Z, color="b", marker="o", label="Projected points in global Oijk")
        # plt.scatter(x, y, c=s)
        # prod_plot = np.log(prod - np.min(prod) + 0.001)
        prod_plot = prod
        # prod_plot = cv2.GaussianBlur(prod_plot, (3, 3), 5)
        # med = np.median(prod_plot)
        # max = np.max(prod_plot)
        # min = np.min(prod_plot)
        # x = np.array(x)[prod_plot < 0.8 * max]
        # y = np.array(y)[prod_plot < 0.8 * max]
        # prod_plot = prod_plot[prod_plot < 0.8 * max]
        # prod_plot = np.log(prod)
        plt.scatter(x, y, c=prod_plot)
        # legend = plt.legend(loc="upper left", shadow=True, fontsize="medium")
        plt.axis("auto")
        plt.title(f"'Zeta' with P = {prime}")
        plt.xlabel("Re", family="serif", color="r", weight="normal", size=16, labelpad=6)
        plt.ylabel("Im", family="serif", color="r", weight="normal", size=16, labelpad=6)
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        os.makedirs("log", exist_ok=True)
        plt.savefig("log/" + timestamp + ".png")
        # plt.show()
        plt.close()

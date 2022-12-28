import os
import time
from datetime import datetime

import cv2
import matplotlib.colors as clr
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from cycler import cycler
from mpl_toolkits import mplot3d

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

    # Colors
    cmap = plt.cm.gist_rainbow
    pace = 0.1
    r_x = 1
    r_y = 15
    real = np.arange(-r_x + pace / 2, r_x, pace)
    imag = np.arange(-r_y + pace / 2, r_y, pace)
    xx, yy = np.meshgrid(real, imag)
    cx = xx.reshape(-1)
    cy = yy.reshape(-1)
    cxy = np.vstack((cx, cy * 1j))
    cj = cx + cy * 1j
    prod = np.ones_like(cx)

    offset_real = 0
    offset_imag = 0
    for prime in PRIMES[:25]:
        s = []
        x = []
        y = []
        n = 1 / (1 - prime ** (-cj))
        # n = 1 / cj
        # prod = n
        prod = prod * n
        X = np.real(prod) - cx
        Y = np.imag(prod) - cy
        Z = np.ones_like(Y)
        CZ = np.vstack((X, Y, Z))
        # S = CZ[0] ** 2 + CZ[1] ** 2 + CZ[2] ** 2
        S = CZ[0] ** 2 + CZ[2] ** 2
        fig = plt.figure(figsize=(10, 10))
        n_plot = prod

        # ax = plt.axes(projection="3d")

        # ax.scatter3D(cx, cy, S, color="b", marker="o", label="Projected points in global Oijk")
        plt.scatter(x=cx, y=cy, c=S)
        plt.title(f"Surface of the function")
        plt.xlabel("Re", family="serif", color="r", weight="normal", size=16, labelpad=6)
        plt.ylabel("Im", family="serif", color="r", weight="normal", size=16, labelpad=6)
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        os.makedirs("log", exist_ok=True)
        plt.savefig("log/" + timestamp + ".png")
        time.sleep(0.5)
        # plt.show()

        plt.close()
        fig = plt.figure(figsize=(10, 10))
        n_plot = prod
        sr = np.real(n_plot)
        si = np.imag(n_plot)

        sr = sr / np.sqrt((sr**2 + si**2))
        si = si / np.sqrt((np.real(n_plot) ** 2 + si**2))
        plt.quiver(
            cx,
            cy,
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
        # plt.show()
    # plt.show()

import os
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


def log_theta(x, z):
    return z * np.log(x) - 2 * np.pi * np.floor(z * np.log(x) / (2 * np.pi))


def im_zeta(x, z):
    return -1 / 2 * (np.sin(z * np.log(x))) / (1 - np.cos(z * np.log(x)))


if __name__ == "__main__":
    x_min = 0.1
    x_max = 290
    pace = 0.1
    x = np.arange(x_min, x_max, pace)

    Z1 = 10
    z_min = 0.01
    z_max = Z1
    z_pace = 0.01
    for z in np.arange(z_min, z_max, z_pace).tolist():
        y = im_zeta(x, z) / np.pi * 180
        primes = np.array(
            [
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
        )
        y_primes = im_zeta(primes, z) / np.pi * 180
        #
        fig = plt.figure(figsize=(10, 7))

        med = np.median(y)
        plt.ylim((-100, 100))
        # plt.xlim((100, 120))

        plt.scatter(x, y, marker="x", color="b")
        plt.scatter(primes, y_primes, marker="o", color="r")
        # legend = fig.legend(loc="upper left", shadow=True, fontsize="medium")
        plt.title(f"Log-theta of primes | z = {z}")
        plt.xlabel("X", family="serif", color="r", weight="normal", size=16, labelpad=6)
        plt.ylabel("Theta", family="serif", color="r", weight="normal", size=16, labelpad=6)
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        os.makedirs("log", exist_ok=True)
        plt.savefig("log/" + timestamp + ".png")
        # plt.show()
        plt.close()

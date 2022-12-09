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


if __name__ == "__main__":
    # Dans un système résonant, les ondes stationnaires de grandes amplitudes ne peuvent plus exister en deça
    # d'une taille donnée. Dans un espace isotrope, chaque fréquence se propage uniformément dans
    # toutes les directions. Si un espace ne peut contenir certaines ondes, c'est que sa taille est trop petite.
    # Donc si cet espace

    x = np.arange(0, 4, 0.001)
    y = np.zeros_like(x)
    factors = [2 ** (x + 1) for x in range(30)]

    # for f in factors:
    #     y += np.cos(f * x)

    for f in factors:
        y = np.cos(f * x)

        fig = plt.figure(figsize=(10, 10))

        plt.plot(x, y)
        plt.title(f"Sum of cosines | Current factor f = {f:.0f}")
        plt.xlabel("X", family="serif", color="r", weight="normal", size=16, labelpad=6)
        plt.ylabel("Y", family="serif", color="r", weight="normal", size=16, labelpad=6)
        plt.ylim((-10, 20))
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        os.makedirs("log", exist_ok=True)
        plt.savefig("log/" + timestamp + ".png")
        time.sleep(1)
        # plt.show()
        plt.close()

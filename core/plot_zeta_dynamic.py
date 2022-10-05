from datetime import datetime

import matplotlib.colors as clr
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from cycler import cycler


def generate_random_vector():
    return np.random.rand(2)


def generate_zeta_vector(ord, pow):
    zeta = 1 / (ord**pow)
    realpart = np.real(zeta)
    imagpart = np.imag(zeta)
    vect = np.array([realpart, imagpart])
    return vect


if __name__ == "__main__":
    n_order = 16

    # Colors
    # get colormap
    cmap = plt.cm.gist_rainbow
    # build cycler with 5 equally spaced colors from that colormap
    c = cycler("color", cmap(np.linspace(0, 1, n_order)))
    # supply cycler to the rcParam
    plt.rcParams["axes.prop_cycle"] = c

    for imag in range(0, 400, 1):
        imag = imag / 10
        plt.figure(figsize=(14, 5))
        complex_power = 0.5 + imag * 1j
        st_point = np.array([0, 0])
        line = st_point
        en_point = st_point
        for i in range(1, n_order):
            vect = generate_zeta_vector(i, complex_power)
            line = np.vstack((en_point, en_point + vect * (-1) ** (i + 1)))
            sb.lineplot(x=line.T[0], y=line.T[1])
            en_point = en_point + vect * (-1) ** (i + 1)

        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        plt.xlim([-1, 3])
        plt.ylim([-3, 3])
        plt.savefig("core/output/" + timestamp + ".png")
        plt.close()

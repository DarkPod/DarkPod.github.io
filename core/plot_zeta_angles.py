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
    plt.figure(figsize=(14, 5))
    n_order = 100
    complex_power = 0.5 + 0.1j

    # Colors
    # get colormap
    cmap = plt.cm.gist_rainbow
    # build cycler with 5 equally spaced colors from that colormap
    c = cycler("color", cmap(np.linspace(0, 1, n_order)))
    # supply cycler to the rcParam
    plt.rcParams["axes.prop_cycle"] = c

    # complex_power = 0.5 + 40.91871901214j
    old_vect = np.array([1, 0])
    for count in range(0, 200, 4):
        angle = []
        orders = []
        plt.figure(figsize=(14, 5))
        plt.xlim([0, 100])
        plt.ylim([-0.5, 4])
        complex_power = 0.5 + count / 100 * 140j
        for i in range(2, n_order):
            vect = generate_zeta_vector(i, complex_power)
            angle.append(np.arccos(np.dot(vect, old_vect) / np.linalg.norm(vect) / np.linalg.norm(old_vect)))
            orders.append(i)
            old_vect = vect * (-1) ** (i + 1)

        sb.pointplot(x=orders, y=angle)
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

        plt.xlabel("Order k", family="serif", color="r", weight="normal", size=16, labelpad=6)
        plt.ylabel("Angle between k and k+1", family="serif", color="r", weight="normal", size=16, labelpad=6)
        plt.xticks([0, 5, 10, 25, 50, 75, 100])
        plt.title(f"Complex power = {complex_power}")
        plt.savefig("core/output/" + timestamp + ".png")
        plt.close()
    a = 0

from datetime import datetime
from email.mime import base

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


def rotate(theta, vect):
    x = np.cos(theta) * vect[0] + np.sin(theta) * vect[1]
    y = np.sin(theta) * vect[0] - np.cos(theta) * vect[1]
    return np.array([x, y])


if __name__ == "__main__":
    plt.figure(figsize=(10, 10))
    n_order = 50
    complex_power = 0.5 + 20.5j

    # get colormap
    cmap = plt.cm.gist_earth
    # build cycler with 5 equally spaced colors from that colormap
    c = cycler("color", cmap(np.linspace(0, 1, n_order)))
    # supply cycler to the rcParam
    plt.rcParams["axes.prop_cycle"] = c
    st_point = np.array([0, 0])
    line = st_point
    en_point = st_point
    angle = []
    base_vect = np.array([1, 0])
    old_vect = np.array([1, 0])
    for i in range(1, n_order):
        plt.figure(figsize=(10, 10))
        points = []
        vect = generate_zeta_vector(i, complex_power)
        angle.append(np.arccos(np.dot(vect, old_vect) / np.linalg.norm(vect) / np.linalg.norm(old_vect)))
        old_vect = -vect  # * (-1) ** (i + 1)
        first_point = np.array([0, 0])
        rotated_vect = base_vect
        # angle = 2
        points.append(first_point)
        plt.xlim([-2, 2])
        plt.ylim([-2, 2])
        line = first_point
        en_point = first_point
        for k in range(1, 40):
            if angle:
                rotated_vect = rotate(k * angle[-1], base_vect)
                line = np.vstack((en_point, en_point + rotated_vect))
                sb.lineplot(x=line.T[0], y=line.T[1])
                en_point = en_point + rotated_vect

                # Strange but interesting, look like a rotation
                # points.append(first_point + rotated_vect)
                # first_point = first_point + rotated_vect
                # sb.pointplot(x=np.array(points[-2:]).T[0], y=np.array(points[-2:]).T[1])

        old_vect = -vect  # * (-1) ** (i + 1)
        plt.title(f"k-th order : {i}")
        plt.xlabel("X", family="serif", color="r", weight="normal", size=16, labelpad=6)
        plt.ylabel("Y", family="serif", color="r", weight="normal", size=16, labelpad=6)
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        plt.savefig("core/output/" + timestamp + ".png")
        plt.close()

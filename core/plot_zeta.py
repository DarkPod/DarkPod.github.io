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
    n_order = 80
    complex_power = 0.5 + 0.1j

    # Colors
    # get colormap
    cmap = plt.cm.gist_rainbow
    # build cycler with 5 equally spaced colors from that colormap
    c = cycler("color", cmap(np.linspace(0, 1, n_order)))
    # supply cycler to the rcParam
    plt.rcParams["axes.prop_cycle"] = c

    complex_power = 0.5 + 14.134725j
    st_point = np.array([0, 0])
    line = st_point
    en_point = st_point
    for i in range(1, n_order):
        vect = generate_zeta_vector(i, complex_power)
        line = np.vstack((en_point, en_point + vect * (-1) ** (i + 1)))
        sb.lineplot(x=line.T[0], y=line.T[1])
        en_point = en_point + vect * (-1) ** (i + 1)

    # complex_power = 0.5 + 14.2j
    # st_point = np.array([0, 0])
    # line = st_point
    # en_point = st_point
    # for i in range(1, n_order):
    #     vect = generate_zeta_vector(i, complex_power)
    #     line = np.vstack((en_point, en_point + vect * (-1) ** (i + 1)))
    #     sb.lineplot(x=line.T[0], y=line.T[1])
    #     en_point = en_point + vect * (-1) ** (i + 1)

    # complex_power = 0.5 + 14.13j
    # st_point = np.array([0, 0])
    # line = st_point
    # en_point = st_point
    # for i in range(1, n_order):
    #     vect = generate_zeta_vector(i, complex_power)
    #     line = np.vstack((en_point, en_point + vect*(-1)**(i+1)))
    #     sb.lineplot(x=line.T[0], y=line.T[1])
    #     en_point = en_point + vect

    plt.title("Line plot")
    plt.show()
    a = 0

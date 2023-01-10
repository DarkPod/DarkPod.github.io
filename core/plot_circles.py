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

# def plot_cir

if __name__ == "__main__":

    c = 0.99
    c_max = 1
    n = 100
    p = 1
    x = np.arange(-n, n + 1, p)
    xy = np.vstack((x, np.zeros_like(x)))

    # r = 2.5
    # theta = np.arange(0, 8 * np.pi, 0.1)
    # x = r * np.cos(theta)
    # y = r * np.sin(theta)
    # xy = np.vstack((x, y))
    # p = np.sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2)
    # radiuses = c * x

    fig, ax = plt.subplots()
    for idx, elem in enumerate(xy.T.tolist()):
        if idx - len(x) / 2 > 0:
            circle2 = plt.Circle((elem[0] * c, elem[1] * c), abs(idx - len(x) / 2) * p * c_max, color="b", fill=False)
        else:
            circle2 = plt.Circle((elem[0] * c, elem[1] * c), abs(idx - len(x) / 2) * p * c_max, color="r", fill=False)
        ax.add_patch(circle2)

    ax.scatter(xy[0] * c, xy[1] * c)
    # # change default range so that new circles will work
    # ax.set_xlim((0, 10))
    # ax.set_ylim((0, 10))

    # ax.add_patch(circle2)
    plt.show()
    # ax.savefig('plotcircles2.png')

    # plt.title(f"'Zeta' with P = {prime}")
    # plt.xlabel("Re", family="serif", color="r", weight="normal", size=16, labelpad=6)
    # plt.ylabel("Im", family="serif", color="r", weight="normal", size=16, labelpad=6)
    # timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    # os.makedirs("log", exist_ok=True)
    # plt.savefig("log/" + timestamp + ".png")
    # time.sleep(0.5)

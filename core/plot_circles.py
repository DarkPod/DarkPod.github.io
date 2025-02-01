import os
import time
from datetime import datetime

import cv2
import matplotlib.colors as clr
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from cycler import cycler
from matplotlib.patches import Ellipse
from mpl_toolkits import mplot3d

# def plot_cir

if __name__ == "__main__":

    for c in range(1, 100):
        c = c / 100
        c_max = 1
        n = 5
        p = 1
        x = np.arange(-n, n + 1, p)
        # x = x * np.sqrt(1 - c**2 / c_max**2)
        xy = np.vstack((x, np.zeros_like(x)))

        # r = 2.5
        # theta = np.arange(0, 8 * np.pi, 0.1)
        # x = r * np.cos(theta)
        # y = r * np.sin(theta)
        # xy = np.vstack((x, y))
        # p = np.sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2)
        # radiuses = c * x
        # plt.figure()
        # ax = plt.gca()

        # ax.add_patch(ellipse)
        beta = 1 / np.sqrt(1 - c**2 / c_max**2)
        # fig, ax = plt.subplots()
        fig, ax = plt.subplots(figsize=(10, 10))
        for idx, elem in enumerate(xy.T.tolist()):
            ray = abs(idx - n) * p * c_max
            if idx - len(x) / 2 > 0:
                # circle2 = plt.Circle((elem[0] * c, elem[1] * c), abs(idx - n) * p * c_max, color="b", fill=False)
                ellipse = Ellipse(
                    xy=(elem[0] * c, elem[1] * c),
                    width=2 * ray * beta,
                    height=2 * ray,
                    edgecolor="b",
                    fc="None",
                    lw=1,
                )
            else:
                # circle2 = plt.Circle((elem[0] * c, elem[1] * c), abs(idx - n) * p * c_max, color="r", fill=False)
                ellipse = Ellipse(
                    xy=(elem[0] * c, elem[1] * c),
                    width=2 * ray * beta,
                    height=2 * ray,
                    edgecolor="r",
                    fc="None",
                    lw=1,
                )
            # ax.add_patch(circle2)
            ax.add_patch(ellipse)

        ax.scatter(xy[0] * c, xy[1] * c)
        # # change default range so that new circles will work
        ax.set_xlim((-10, 10))
        ax.set_ylim((-10, 10))

        # ax.add_patch(circle2)
        # plt.show()
        # ax.savefig('plotcircles2.png')

        plt.title(f"Beta = {beta:.3f}, speed = {c*100:3f}%")
        plt.xlabel("X", family="serif", color="r", weight="normal", size=16, labelpad=6)
        plt.ylabel("Y", family="serif", color="r", weight="normal", size=16, labelpad=6)
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        os.makedirs("log", exist_ok=True)
        plt.savefig("log/" + timestamp + ".png")
        # time.sleep(0.5)

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


class surface:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        s = point1[1] - point2[1] / point1[0] - point2[0]
        b = point1[1] - s * point1[0]
        self.a = -s
        self.b = 1
        self.c = -b


def check_intersect(ray, map_elem):
    s = (ray[0, 0] - ray[0, 1]) / (ray[1, 0] - ray[1, 1])
    b = ray[0, 1] - s * ray[0, 0]
    a1 = -s
    b1 = 1
    c1 = -b
    a2 = map_elem.a
    b2 = map_elem.b
    c2 = map_elem.c
    v1 = np.array([a1, b1])
    v1 = v1 / np.linalg.norm(v1)
    v2 = np.array([a2, b2])
    v2 = v2 / np.linalg.norm(v2)
    angle = np.arccos(np.dot(v1, v2))
    inter = np.array([(b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1), (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)])
    return inter, angle


def raytrace(instant, position, angle, map):
    x = np.vstack((position, position + instant * np.array([np.cos(angle), np.sin(angle)])))
    len1 = np.sqrt((x[0, 0] - x[1, 0]) ** 2 + (x[0, 1] - x[1, 1]) ** 2)
    for elem in map:
        inter, angle = check_intersect(x, elem)
        if ((inter[0] < x[0, 0]) & (inter[0] > x[1, 0])) | ((inter[0] > x[0, 0]) & (inter[0] < x[1, 0])):
            if ((inter[1] < x[0, 1]) & (inter[1] > x[1, 1])) | ((inter[1] > x[0, 1]) & (inter[1] < x[1, 1])):
                # Mettre de côté l'ancien segment
                print(angle / 2 / np.pi * 360)
                x = np.vstack((position, inter))
                len2 = np.sqrt((x[0, 0] - x[1, 0]) ** 2 + (x[0, 1] - x[1, 1]) ** 2)
                # Tracer le nouveau et vérifier son intersection
                # Recurrence

    plt.plot(x.T[0], x.T[1])
    return x


def plot_circle(instant, position, map):
    angles = np.arange(0, 2 * np.pi, 0.1)
    x = []
    for theta in angles:
        x.append(raytrace(instant, position, theta, map))
    x = np.array(x)
    plt.scatter(x.T[0], x.T[1])
    a = 0


if __name__ == "__main__":
    # Colors
    # get colormap
    cmap = plt.cm.gist_rainbow
    # build cycler with 5 equally spaced colors from that colormap
    c = cycler("color", cmap(np.linspace(0, 1, int(20 * np.pi + 1))))
    # supply cycler to the rcParam
    plt.rcParams["axes.prop_cycle"] = c

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
    # for idx, elem in enumerate(xy.T.tolist()):
    #     if idx - len(x) / 2 > 0:
    #         circle2 = plt.Circle((elem[0] * c, elem[1] * c), abs(idx - len(x) / 2) * p * c_max, color="b", fill=False)
    #     else:
    #         circle2 = plt.Circle((elem[0] * c, elem[1] * c), abs(idx - len(x) / 2) * p * c_max, color="r", fill=False)
    #     ax.add_patch(circle2)

    # ax.scatter(xy[0] * c, xy[1] * c)
    # # change default range so that new circles will work
    # ax.set_xlim((0, 10))
    # ax.set_ylim((0, 10))
    # plot_circle(instant=2.5, position=np.array([0, 0]), map=None)
    my_map = []
    my_map.append(surface([5, -5], [5, 5]))
    stop = 10
    for i in range(0, stop + 1):
        plot_circle(instant=c_max * (i - stop / 2), position=c * np.array([i - stop / 2, 0]), map=my_map)
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

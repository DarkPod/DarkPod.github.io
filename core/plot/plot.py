# Go to pandas
# Use seaborn
import os
import time
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np


def vector(xy, uv, title="", xlabel="", ylabel="", log=False):
    fig = plt.figure(figsize=(10, 10))
    uv = uv / np.sqrt((uv[0] ** 2 + uv[1] ** 2))
    plt.quiver(
        xy[0],
        xy[1],
        uv[0],
        uv[1],
        # label=""
    )
    # legend = plt.legend(loc="upper left", shadow=True, fontsize="medium")
    # plt.axis("auto")
    # plt.plot([-1, 1], [14.13, 14.13])
    plt.title(title)
    plt.xlabel(xlabel, family="serif", color="r", weight="normal", size=16, labelpad=6)
    plt.ylabel(ylabel, family="serif", color="r", weight="normal", size=16, labelpad=6)
    if log:
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        os.makedirs("log", exist_ok=True)
        plt.savefig("log/" + timestamp + ".png")
        time.sleep(0.5)
    # plt.show()


def scatter():
    pass

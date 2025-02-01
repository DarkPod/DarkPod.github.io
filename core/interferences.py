import glob
import os
from datetime import datetime

import cv2
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    size = np.array([128, 128, 40])
    center = size / 2
    wave_vector = 2 * np.pi / 8
    second_source = np.array([13, 30])
    img = np.zeros(size)
    for x in range(size[0]):
        for y in range(size[1]):
            img[x, y] = np.cos(((x - center[0]) ** 2 + (y - center[1]) ** 2) ** (1 / 2) * wave_vector)

    fig = plt.figure(figsize=(10, 10))
    plt.imshow(img[:, :, 0])
    plt.title(f"Spherical wave with with \u03BB = {1/wave_vector*2*np.pi}")
    plt.xlabel("x", family="serif", color="r", weight="normal", size=16, labelpad=6)
    plt.ylabel("y", family="serif", color="r", weight="normal", size=16, labelpad=6)
    timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    os.makedirs("log", exist_ok=True)
    plt.savefig("log/" + timestamp + ".png")
    # plt.show()
    plt.close()

    # Interferences

    img = np.zeros(size)
    for x in range(size[0]):
        for y in range(size[1]):
            img[x, y] = np.cos(((x - center[0]) ** 2 + (y - center[1]) ** 2) ** (1 / 2) * wave_vector) + np.cos(
                ((x - center[0] - second_source[0]) ** 2 + (y - center[1] - second_source[1]) ** 2) ** (1 / 2)
                * wave_vector
            )

    fig = plt.figure(figsize=(10, 10))
    plt.imshow(img[:, :, 0])
    plt.title(f"Amplitude interferences wave with with \u03BB = {1/wave_vector*2*np.pi}")
    plt.xlabel("x", family="serif", color="r", weight="normal", size=16, labelpad=6)
    plt.ylabel("y", family="serif", color="r", weight="normal", size=16, labelpad=6)
    timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    os.makedirs("log", exist_ok=True)
    plt.savefig("log/" + timestamp + ".png")
    # plt.show()
    plt.close()

    # Intensity projected on a plane
    intensity_map = img[:, :, 0] ** 2
    intensity_map = intensity_map
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(intensity_map)
    plt.title(f"Spherical wave with with \u03BB = {1/wave_vector*2*np.pi}")
    plt.xlabel("x", family="serif", color="r", weight="normal", size=16, labelpad=6)
    plt.ylabel("y", family="serif", color="r", weight="normal", size=16, labelpad=6)
    timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    os.makedirs("log", exist_ok=True)
    plt.savefig("log/" + timestamp + ".png")
    # plt.show()
    plt.close()

    # Mean intensity projected on a plane
    c = 100
    img = np.zeros(size)
    for t in range(size[2]):
        for x in range(size[0]):
            for y in range(size[1]):
                img[x, y, t] = np.cos(
                    ((x - center[0]) ** 2 + (y - center[1]) ** 2) ** (1 / 2) * wave_vector + c * t
                ) + np.cos(
                    ((x - center[0] - second_source[0]) ** 2 + (y - center[1] - second_source[1]) ** 2) ** (1 / 2)
                    * wave_vector
                    + c * t
                )
    intensity_map = img**2
    for t in range(size[2]):

        fig = plt.figure(figsize=(10, 10))
        plt.imshow(intensity_map[:, :, t])
        plt.title(f"Spherical wave with with \u03BB = {1/wave_vector*2*np.pi}")
        plt.xlabel("x", family="serif", color="r", weight="normal", size=16, labelpad=6)
        plt.ylabel("y", family="serif", color="r", weight="normal", size=16, labelpad=6)
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        os.makedirs("log", exist_ok=True)
        plt.savefig("log/" + timestamp + ".png")
        # plt.show()
        plt.close()

    intensity_map = np.mean(intensity_map, axis=2)
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(intensity_map)
    plt.title(f"Spherical wave with with \u03BB = {1/wave_vector*2*np.pi}")
    plt.xlabel("x", family="serif", color="r", weight="normal", size=16, labelpad=6)
    plt.ylabel("y", family="serif", color="r", weight="normal", size=16, labelpad=6)
    timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    os.makedirs("log", exist_ok=True)
    plt.savefig("log/" + timestamp + ".png")
    # plt.show()
    plt.close()
    a = 0

    # On a plane
    fig = plt.figure(figsize=(10, 10))
    plt.plot(intensity_map[:, 127])
    plt.title(f"Spherical wave with with \u03BB = {1/wave_vector*2*np.pi}")
    plt.xlabel("y", family="serif", color="r", weight="normal", size=16, labelpad=6)
    plt.ylabel("I", family="serif", color="r", weight="normal", size=16, labelpad=6)
    timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    os.makedirs("log", exist_ok=True)
    plt.savefig("log/" + timestamp + ".png")
    # plt.show()
    plt.close()
    a = 0

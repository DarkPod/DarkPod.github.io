import glob
import os

import cv2
import numpy as np

if __name__ == "__main__":
    frame_size = (1000, 1000)
    os.makedirs("core/output", exist_ok=True)
    out = cv2.VideoWriter("core/output/sum_cos_with_substraction.avi", cv2.VideoWriter_fourcc(*"DIVX"), 5, frame_size)

    for filename in glob.glob("log/*.png"):
        img = cv2.imread(filename)
        out.write(img)

    out.release()

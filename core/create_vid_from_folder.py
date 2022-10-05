import glob

import cv2
import numpy as np

if __name__ == "__main__":
    frame_size = (1400, 500)

    out = cv2.VideoWriter("core/output/zeta_video.avi", cv2.VideoWriter_fourcc(*"DIVX"), 10, frame_size)

    for filename in glob.glob("core/output/*.png"):
        img = cv2.imread(filename)
        out.write(img)

    out.release()

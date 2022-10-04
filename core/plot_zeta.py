
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
if __name__ == "__main__":
    st_point = np.array([0,1])
    line = st_point
    en_point = st_point
    for i in range(10):
        x_vect = np.random.rand()
        y_vect = np.random.rand()
        vect = np.array([x_vect,y_vect])
        vect = vect / np.linalg.norm(vect)
        en_point = en_point + vect
        line = np.vstack((line, en_point))
    plt.figure(figsize=(14, 5))

    sb.lineplot(x = line.T[0], y = line.T[1]
                )

    plt.title("Line plot")
    plt.show()
    a=0

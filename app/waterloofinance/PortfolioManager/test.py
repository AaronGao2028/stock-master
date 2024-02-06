import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

A = [45, 37, 42, 35, 39]
B = [38, 31, 26, 28, 33]
C = [10, 15, 17, 21, 12]
D = [10, 15, 17, 21, 12]

data = np.array([A, B, C, D])

cov_matrix = np.cov(data,bias=True)
sn.heatmap(cov_matrix, annot=True, fmt='g')
plt.show()
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
lables = ["Apple", "Orange", "Banana", "Strawberry"]

plt.pie(x, labels=lables)
plt.show()

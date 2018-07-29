import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = [2, 5, 10]
y = [10, 2, 15]
z = [10, 5, 10]

plt.plot(x, y)
plt.scatter(x, z)

plt.title("Abdullah")
plt.xlabel("X")
plt.ylabel("Y")

plt.legend(["This is Y", "This is Z"])
plt.show()

plt.hist(x)

# cars = pd.read_csv('cars.csv', index_col=0)


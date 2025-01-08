import matplotlib.pyplot as plt

import numpy as np
import random 

x = np.random.randint(10,60,(50))
#((start,stop(number of item))
print(x)

number = [23,34,55,24,56,85,89,74,12,32,58,21,54,78,95,124,789]

plt.hist(number,color="r",edgecolor="g",cumulative=-1,bottom=10, align="left",label="Python")
#histype="step","stepfilled","barstacked","bar".orientation="horizontal".log=True.
plt.title("Python")
plt.xlabel("PYTHON")
plt.ylabel("Number")

plt.axvline(45,color="b")
plt.grid()

plt.legend()
plt.show()

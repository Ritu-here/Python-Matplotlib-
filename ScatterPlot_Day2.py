#Scatter Plot
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [2,3,1,4,3,6,2]
z = [3,2,4,5,1,6,2]
plt.scatter(x,y , color="r", s=300, alpha=1,marker="*", edgecolor="g",linewidth=2)
plt.scatter(x,y , color="b", s=200, alpha=1,marker=".", edgecolor="y",linewidth=2)
plt.colorbar()
plt.title("Scatter PLot", fontsize=15)
plt.xlabel("Day", fontsize=10)
plt.ylabel("Number", fontsize=10)
plt.show()

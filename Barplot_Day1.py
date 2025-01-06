#Bar Plot


import matplotlib.pyplot as plt
import numpy as np

x=["python","c++","c","java","javascript"]
y=[85,70,60,82,55]
z=[20,30,40,50,55]
width = 0.2
p=np.arange(len(x))
p1=[j+width for j in p]
plt.xlabel("language",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("Demands", fontsize=15)


# plt.bar(x,y,width=0.5,color=c ,align="center", edgecolor="r",linewidth=5,linestyle=":",label="demands")
plt.bar(x,y,width,color="r" ,linewidth=5,label="demands")
plt.bar(p1,z,width,color="y" ,linewidth=5,label="demands1")
plt.xticks(p+width/2,x,rotation=10)
plt.legend()
plt.show()


#Horizontal Bar Graph
"""

import matplotlib.pyplot as plt
import numpy as np

x=["python","c++","c","java","javascript"]
y=[85,70,60,82,55]
z=[20,30,40,50,55]
width = 0.2
p=np.arange(len(x))
p1=[j+width for j in p]
plt.xlabel("language",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("Demands", fontsize=15)


# plt.bar(x,y,width=0.5,color=c ,align="center", edgecolor="r",linewidth=5,linestyle=":",label="demands")
plt.barh(x,y,width,color="r" ,linewidth=5,label="demands")
plt.barh(p1,z,width,color="y" ,linewidth=5,label="demands1")
plt.xticks(p+width/2,x,rotation=10)
plt.legend()
plt.show()
"""
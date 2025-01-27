import matplotlib.pyplot as plt
x = [10,20,30,40]
y = ["c","c++","java","python"]
ex=[0.4,0.0,0.0,0.0]
c=["r","g","b","y"]
plt.pie(x , labels=y, explode=ex, colors=c,autopct="%0.1f%%", shadow=3,textprops={"fontsize":15},
        wedgeprops={"linewidth":8,})

#startingsngle=90,shadow=3, radius=1,labeldistance=1.2,counterclock=false,center=(1,3),wedgeprops={"linewidth":8,"edgecolor":"m"}
#rotatelabels=false
plt.title("Language understanding")
plt.legend(loc=2)
plt.show()


#Dot Pie Chart
plt.pie([1])
plt.show()
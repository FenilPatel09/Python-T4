import matplotlib.pyplot as plt
import numpy as np
# x=np.array([1,8])
# y=np.array([3,10])
# plt.plot(x,y,marker='o')
# plt.show()

# y=[3,8,1,10,5,7]
# plt.plot(y,marker='D',ms=10,color='green',mec='k',mfc='y',linestyle="dashed")
# y1=[6,2,7,6,8,3]
# plt.plot(y1)
# plt.show()

# x1=np.array([0,1,2,3])
# y1=np.array([3,8,1,10])
# x2=np.array([0,1,2,3])
# y2=np.array([6,2,7,11])
# plt.plot(x1,y1,x2,y2)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("line chart",fontdict={"family":"serif","color":"darkred","size":15},loc="left")
# plt.grid(axis="x")
# plt.show()

# x=np.array([5,7,8,3,17,3,5,7,8,12,6,7,8,4])
# y=np.array([99,89,67,111,90,78,80,66,77,89,89,78,67,56])
# plt.scatter(x,y)
# plt.show()

# x=np.random.randint(100,size=(100))
# y=np.random.randint(100,size=(100))
# colors=np.random.randint(100,size=(100))
# sizes=10*np.random.randint(100,size=(100))
# plt.scatter(x,y,c=colors,s=sizes)
# plt.colorbar()
# plt.show()

x=np.array([0,0,1,1,1,1,4,4,2,2,2,3,3,5])
plt.hist(x)
plt.show()

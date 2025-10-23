#algorithm for bender-schmidt Equation
import numpy as np
import matplotlib.pyplot as plt
h=0.25
k=0.25
x=np.arange(0,1+h,h)
y=np.arange(0,1+k,k)
n=len(x)
m=len(y)
Temp=np.zeros((m,n))
Temp[0,:]=np.sin(np.pi*x)
Temp[:,0]=0
Temp[:,-1]=0
lamda=k/(h**2)
for j in range(1,m):
    for i in range(1,n-1):
        Temp[j,i]=(lamda*Temp[j-1,i-1]+(1-2*lamda)*Temp[j-1,i]+lamda*Temp[j-1,i+1])
print("Temperature Distribution:")
print(Temp)

X,Y=np.meshgrid(x,y)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Temp,facecolor='red')
ax.set_xlabel('x (Distance)')
ax.set_ylabel('y (Time)')
ax.set_zlabel('Temperature')
ax.set_title('Bender-schmidt Solution')
plt.show()
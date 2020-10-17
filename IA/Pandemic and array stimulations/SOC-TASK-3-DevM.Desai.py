from random import seed
from random import randint
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter 

# seed random number generator
seed(1)

dx=[0]
n1=[]
a1=[]  #y axis variable


for i1 in range(500):
    a1.append(i1)
    n1.append(0)
    no_of_1=[1]
    a=[0]
    for i in range(9999):
        a.append(0)
    a[5000]=1
    while(1):
        #swapping
        for j in range(5):
           x=randint(0,9999)
           y=randint(0,9999)
           a[x]=a[y]+a[x]
           a[y]=a[x]-a[y]
           a[x]=a[x]-a[y]
        #the magic basically adding 1s
        for i in range(10000):
           if(a[i]==1):
               if(randint(0,19)<7):
                   a[i-1]=1
               elif(randint(0,19)<7):
                   a[(i+1)%10000]=1
        n1[i1]=n1[i1]+1
        #caz lists go out of range
        no_of_1.append(0)
        #counting 1s
        for i in range(10000):
           if(a[i]==1):
              no_of_1[n1[i1]]=no_of_1[n1[i1]] + 1
        if(a1[-1]==0):
           dx.append(no_of_1[n1[i1]]-no_of_1[n1[i1]-1])
        if((int)(no_of_1[n1[i1]])==10000):
           break
    if(a1[-1]==0):
        x1=[1]  #x axis variable
        for i in range(n1[0]):
           x1.append(i+2)
        plt.plot(x1,no_of_1,)
        plt.xlabel('no of repetitions')
        plt.ylabel('no of 1s')
        plt.show()
        plt.plot(x1,dx,color='yellow')
        plt.xlabel('x')
        yhat=savgol_filter(dx, 51, 1)
        plt.ylabel('dx')
        plt.plot(x1,yhat,color='red')
        plt.show()
        maxi=0
        maxy=0
        for i in range(n1[0]):
            if(dx[i]>maxi):
                maxi=dx[i]
                maxy=yhat[i]
        print(maxy)

#plotting
plt.plot(a1,n1)
plt.ylabel('no of repetitions')
plt.xlabel('no of iterations')
plt.show()

sum=0
for i in range(500):
    sum=sum+n1[i]/500
print(sum)


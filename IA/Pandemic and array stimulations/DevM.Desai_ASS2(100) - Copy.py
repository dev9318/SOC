from random import seed
from random import randint
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter 

# seed random number generator
seed(1)

a = [[0 for i in range(150)] for j in range(100)]
a__ = [[0 for i in range(150)] for j in range(100)]
dx=[0]
a[50][75]=1
a__[50][75]=1
x2=[]
n1=[]
for i in range(100):
    n1.append(0)
    x2.append(i)
    no_1=[]
    print(a)
    while(1):
        no_1.append(0)
        for i1 in range(8):
            a1=randint(0,99)
            b=randint(0,99)
            a11=randint(0,149)
            b1=randint(0,149)
            a[a1][a11]=a[a1][a11]+a[b][b1]
            a[b][b1]=a[a1][a11]-a[b][b1]
            a[a1][a11]=a[a1][a11]-a[b][b1]
        for i1 in range(100):
            for j in range(150):
                if(a[i1][j]==1):
                    for i2 in range(5):
                        for j1 in range(5):
                            if((i2>0 and i2<4 and j1>0 and j1<4) and (randint(0,3)<1)):
                                a__[(i1+i2-2)%100][(j+j1-2)%150]=1
                            elif(not (i2>0 and i2<4 and j1>0 and j1<4) and (randint(0,24)<2)):
                                a__[(i1+i2-2)%100][(j+j1-2)%150]=1
        for i1 in range(100):
            for j in range(150):
                a[i1][j]=a__[i1][j]
        for i1 in range(100):
            for j in range(150):
                if(a[i1][j]==1):
                    no_1[n1[i]]=no_1[n1[i]] + 1
        if(i==0):
           dx.append(no_1[n1[i]]-no_1[n1[i]-1])
        if(no_1[n1[i]]==15000):
            for i1 in range(100):
                for j in range(150):
                    a[i1][j]=0
                    a__[i1][j]=0
            a[50][75]=1
            a__[50][75]=1
            break
        n1[i]=n1[i]+1
    if(i==0):
        x1=[]
        for i1 in range(n1[i]+1):
            x1.append(i1)
        plt.plot(x1,no_1)
        plt.xlabel('no of repetitions')
        plt.ylabel('no of 1s')
        plt.show()
        x1.append(n1[i]+1)
        plt.plot(x1,dx,color='yellow')
        plt.xlabel('x')
        #yhat=savgol_filter(dx, 51, 3)
        plt.ylabel('dx')
        #plt.plot(x1,yhat,color='red')
        plt.show()
        maxi=0
        #maxy=0
        for i in range(n1[0]):
            if(dx[i]>maxi):
                maxi=dx[i]
                #maxy=yhat[i]
        print(maxi)

#plotting
plt.plot(x2,n1)
plt.ylabel('no of repetitions')
plt.xlabel('no of iterations')
plt.show()

sum=0
for i in range(100):
    sum=sum+n1[i]/100
print(sum)

                            
        



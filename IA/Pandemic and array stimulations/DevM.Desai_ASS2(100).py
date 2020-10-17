from random import seed
from random import randint
import matplotlib.pyplot as plt 

# seed random number generator
seed(1)


n1=[]
a1=[]  #y axis variable


for i1 in range(10000):
    a1.append(i1)
    n1.append(0)
    no_of_1=[1]
    a=[0]
    for i in range(999):
        a.append(0)
    a[217]=1
    while(1):
        #the magic basically adding 1s
        for i in range(1000):
           if(a[i]==1):
               if(randint(0,1)==0):
                   a[i-1]=1
               else:
                   a[(i+1)%1000]=1
        #swapping
        x=randint(0,999)
        y=randint(0,999)
        a[x]=a[y]+a[x]
        a[y]=a[x]-a[y]
        a[x]=a[x]-a[y]
        n1[i1]=n1[i1]+1
        #caz lists go out of range
        no_of_1.append(0)
        #counting 1s
        for i in range(1000):
           if(a[i]==1):
              no_of_1[n1[i1]]=no_of_1[n1[i1]] + 1
        if((int)(no_of_1[n1[i1]])==1000):
           break

#plotting
plt.plot(a1,n1)
plt.ylabel('no of repetitions')
plt.xlabel('no of iterations')

sum=0.0
for i in range(10000):
    sum=sum+n1[i]/10000
print(sum)

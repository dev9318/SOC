from random import seed, randint, random
import copy
import matplotlib.pyplot as plt

seed(1)

a=[]


lens=[[330,500],[232,400],[215,400],[377,200],[300,200],[298,200],[283,200],[252,200],[249,200],[204,200],[173,200],[144,200],[138,200],[136,200],[129,200],[183,125],[168,125],[167,125],[83,100],[57,100],[60,50],[50,50],[42,50],[32,50],[48,25],[44,25],[36,25],[20,25],[139,100]]
ab=[]
for i1 in range(29):
    ab.append([[]])
    ab[i1] = [[0 for i in range(lens[i1][1])] for j in range(lens[i1][0])]
    for i2 in range(10):
        ab[i1][10+i2][i2*2]=1
total=0

no_in=[]
n=-1
prob=[0.0828,0.0365,0.1102,0.1029,0.0236,0.0555,0.0201,0.0319,0.0303,0.0201,0.0319,0.0308,0.0303,0.0269,0.0307,0.0859,0.0414,0.0397,0.0556,0.0189,0.0573,0.0189,0.0123,0.0350,0.0132,0.0122,0.0122,0.0119,0.0394,0.0017,0.0052,0.0086,1]
no_in_t=290
no_hos=0

while(1):
    a.append(copy.deepcopy(ab))
    no_in=0
    n=n+1
    no_hos=0
    print(n)
    if(n<5):
        for i in range(1280000):
            x= randint(0,28)
            b= randint(0,lens[x][0]-1)
            c= randint(0,lens[x][1]-1)
            x1= randint(0,28)
            b1= randint(0,lens[x1][0]-1)
            c1= randint(0,lens[x1][1]-1)
            if((ab[x][b][c] or ab[x1][b1][c1])and n>0):
                for i in range(n):
                    a[n-i][x][b][c]= a[n-i][x][b][c]+a[n-i][x1][b1][c1]
                    a[n-i][x1][b1][c1]= a[n-i][x][b][c]-a[n-i][x1][b1][c1]
                    a[n-i][x][b][c]= a[n-i][x][b][c]-a[n-i][x1][b1][c1]
            ab[x][b][c]= ab[x][b][c]+ab[x1][b1][c1]
            ab[x1][b1][c1]= ab[x][b][c]-ab[x1][b1][c1]
            ab[x][b][c]= ab[x][b][c]-ab[x1][b1][c1]
    else:
        for i in range(3200):
            x= randint(0,28)
            b= randint(0,lens[x][0]-1)
            c= randint(0,lens[x][1]-1)
            x1= randint(0,28)
            b1= randint(0,lens[x1][0]-1)
            c1= randint(0,lens[x1][1]-1)
            if((ab[x][b][c] or ab[x1][b1][c1])and n>0):
                for i in range(n):
                    a[n-i][x][b][c]= a[n-i][x][b][c]+a[n-i][x1][b1][c1]
                    a[n-i][x1][b1][c1]= a[n-i][x][b][c]-a[n-i][x1][b1][c1]
                    a[n-i][x][b][c]= a[n-i][x][b][c]-a[n-i][x1][b1][c1]
            ab[x][b][c]= ab[x][b][c]+ab[x1][b1][c1]
            ab[x1][b1][c1]= ab[x][b][c]-ab[x1][b1][c1]
            ab[x][b][c]= ab[x][b][c]-ab[x1][b1][c1]
    for x in range(29):
        for i in range(lens[x][0]):
            for j in range(lens[x][1]):
                if(ab[x][i][j]==1 or ab[x][i][j]==2 or ab[x][i][j]==3):
                    for i1 in range(3):
                        for j1 in range(3):
                            if((ab[x][(i-1+i1)%lens[x][0]][(j-1+j1)%lens[x][1]]==0) and random()<prob[x]*1.2):
                                ab[x][(i-1+i1)%lens[x][0]][(j-1+j1)%lens[x][1]]=1
    for x in range(29):
        for i in range(lens[x][0]):
            for j in range(lens[x][1]):
                if(ab[x][i][j]==3):
                    no_hos = no_hos +1
    if(n>=0):
        for x in range(29):
            for i in range(lens[x][0]):
                for j in range(lens[x][1]):
                    if(ab[x][i][j]==1):
                        if(no_hos>=12000):
                            ab[x][i][j]=2 #not hospitalized
                        else:
                            ab[x][i][j]= 3 # hospitalized
    if(n>5):
        for x in range(29):
            for i in range(lens[x][0]):
                for j in range(lens[x][1]):
                    if(a[n-6][x][i][j]==2 or a[n-6][x][i][j]==3):
                        if(0.05>random()):
                            ab[x][i][j]= 5 #dead
                        else:
                            ab[x][i][j]= 4
                    
        
    for x in range(29):
        for i in range(lens[x][0]):
            for j in range(lens[x][1]):
                if(ab[x][i][j]==3 or ab[x][i][j]==2):
                    no_in=no_in+1
    print(no_in)    
    if( n>150):
        break

for x in range(28):
    nodead=[]
    abc=0
    x1=[]
    for y in range(n):
        x1.append(y)
        for i in range(lens[x][0]):
            for j in range(lens[x][1]):
                if(a[y][x][i][j]==5):
                    abc=abc+1
                
        nodead.append(abc)
    if(x==0 or x==2 or x==3 or x==28 or x==15):
        plt.plot(x1,nodead)
        plt.title(x)
        plt.ylabel('no of deaths')
        plt.xlabel('no of days')

        plt.show()
    

    

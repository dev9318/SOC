def update(Song1 ,Song2):
    alpha= 0.01
    for i in range(1,5): 
        Song2[i] =Song2[i] + alpha*(Song2[i]-Song1[i])
def onsearch(Song1, Song2):
    alpha= 0.01
    for i in range(1,5): 
        Song2[i] =Song2[i] - alpha*(Song2[i]-Song1[i])

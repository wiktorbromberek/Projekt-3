import random
n=5




def matrix(n):
    xd=int(1/2*(n*(n-1)/2))
    l=[]
    for i in range(n):
        lista=[0]*n
        l.append(lista)
    count=0
    while count < xd:
        wiersz=random.randint(0,n-2)
        kolumna=random.randint(wiersz+1,n-1)
        print(wiersz,kolumna)
        if l[wiersz][kolumna] ==0:
            l[wiersz][kolumna]=1
            count+=1



    return l


l=matrix(n)
for i in range(n):
    print(l[i])

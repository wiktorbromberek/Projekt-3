import random
n=4




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
        #print(wiersz,kolumna)
        if l[wiersz][kolumna] ==0:
            l[wiersz][kolumna]=1
            count+=1
    return l

def dosoutin(m):
    l=[]
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j]==1:
                l.append([i,j])
    return l


def lista_nastepnikow(m):
    l=[]
    for i in range(len(m)):
        l1=[]
        for j in range(len(m)):
            if m[i][j]==1:
                l1.append(j)
        l1.append(".")
        l.append(l1)
    return l






l=matrix(n)
print()
print("Macierz sąsiedztwa")
print()
for i in range(n):
    print(l[i])
lista=dosoutin(l)
print()
print("------|-------")
print()
print("Tabela krawędzi")
print()
for i in range(len(lista)):
    print(lista[i])
print()
print("------|-------")
print()
lista_kolejna=lista_nastepnikow(l)
print("Lista następników")
print()
for i in range(len(lista_kolejna)):
    print(lista_kolejna[i])

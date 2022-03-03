def generator(n, k=0):
    while k<=n:
        if k%2==0:
            yield k
        k+=1
n=int(input())
l=[]
for i in generator(n):
    l.append(str(i))
print(','.join(l))
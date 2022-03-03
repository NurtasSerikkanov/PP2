def gen(n, k=1):
    while k<=n:
        yield k**2
        k+=1
n=int(input())
g=gen(n)
for i in g:
    print(i)
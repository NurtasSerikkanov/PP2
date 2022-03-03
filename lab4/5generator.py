def generator(n):
    while n>=0:
        yield n
        n-=1
n=int(input())
g=generator(n)
for i in g:
    print(i, end=' ')
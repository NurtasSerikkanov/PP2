def generator(a, b):
    while a<=b:
        yield a**2
        a+=1
a=int(input())
b=int(input())
g=generator(a, b)
for i in g:
    print(i, end=' ')
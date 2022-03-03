def isPrime(n):
    if n<=1: return False
    for i in range(2, n/2+1):
        if n%i==0:
            return False
    return True

def Prime(l):
    p=[]
    for i in l:
        for j in i:
            if isPrime(j):
                p.append(j)
    return p

l=list(map(int,input().split()))
print(Prime(l))

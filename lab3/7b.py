def name(l):
    for i in range(len(l)):
        if l[i:i+2]==[3, 3]:
            return True
    return False
n=list(map(int, input().split()))
print(name(n))

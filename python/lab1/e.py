def prime(a):
    if a==1 or a==0: return False
    for i in range(2, int(a/2)+1):      #i=2 i<=n/2; i++
        if a%i==0:
            return False
    return True

a, b = map(int, input().split())       #type(a)=int type(b)=int
if a<=500 and prime(a) and b%2==0:      
    print("Good job!")
else:
    print("Try next time!")

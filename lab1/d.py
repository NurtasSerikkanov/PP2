a=float(input())        # a=2.8
z=input()               # z=str
if z=='k':
    c=int(input())      # c=int
    b=a/1024
    print(round(b, c))  # b=5.465515454 c=3   print -- 5.465
if z=='b':
    print(a*1024)
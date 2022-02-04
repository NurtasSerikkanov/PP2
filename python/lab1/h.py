s, t = input(), input()   #s, t =str
x=s.find(t)               
y=s.rfind(t)
if x==y:                  # s=lucky t=c --> x=2 y=2 --> x==y
    print(x)
else:
    print(x, y)
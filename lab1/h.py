s, t = input(), input()
x=s.find(t)
y=s.rfind(t)
if x==y:
    print(x)
else:
    print(x, y)
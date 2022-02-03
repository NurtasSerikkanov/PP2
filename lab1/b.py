s=input()
a=0
for i in s:                   
    a+=ord(i)                 #"a"=97, "A"=65  a=95, a=95+67
if a>300:
    print("It is tasty!")
else:
    print("Oh, no!")
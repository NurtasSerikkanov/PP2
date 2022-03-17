s=input()
lower=0
upper=0
for i in s:
    if i.islower():
        lower+=1
    if i.isupper():
        upper+=1
print(lower)
print(upper)
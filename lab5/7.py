import re
text=input()
pattern=r'[a-z][^_]*'
ls=re.findall(pattern, text)
res=" "
for i in ls:
    res+=i.capitalize()
print(res)
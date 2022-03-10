import re
text=input()
ls=re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
res=""
for i in ls:
    res+=i.lower()
print(res)
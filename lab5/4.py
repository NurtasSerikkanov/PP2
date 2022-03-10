import re
pattern='[A-Z]+[a-z]+'
text=input()
res=re.search(pattern, text)
print('YES' if res else 'NO')
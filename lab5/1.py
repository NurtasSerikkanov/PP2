import re
pattern='^a(b*)$'
text=input()
res=re.search(pattern, text)
print('YES' if res else 'NO')
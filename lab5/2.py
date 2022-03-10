import re
pattern='^a(b{2,3})$'
text=input()
ls=re.search(pattern, text)
print('YES' if ls else 'NO')
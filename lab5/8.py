import re
text='MyNameIsNurtas'
pattern='[A-Z][^A-Z]+'
ls=re.findall(pattern, text)
print(ls)
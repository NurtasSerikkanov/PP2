import re
text='MyNameIsNurtas'
pattern='[A-Z][a-z]+'
ls=re.findall(pattern, text)
print(' '.join(ls))
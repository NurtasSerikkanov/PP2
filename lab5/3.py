import re
pattern='^[a-z]+_[a-z]+$'
text='aab_abbbc'
res=re.search(pattern, text)
print('Found a match!' if res else 'Not matched!')
import os
cnt=0
with open('file', 'r') as f:
    for line in f:
            cnt+=1
print(cnt)
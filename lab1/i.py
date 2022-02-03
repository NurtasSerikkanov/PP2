def name(s):
    for i in s:
        if s.endswith("@gmail.com"):
            return True
    return False

n=int(input())
for i in range(n):
   s=input()
   if name(s):
       print(s[:-10])
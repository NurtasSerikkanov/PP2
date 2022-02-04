def name(s):
    for i in s:
        if s.endswith("@gmail.com"):         #find
            return True
    return False

n=int(input())
for i in range(n):
   s=input()
   if name(s):
       print(s[:-10])                #Nurtas@gmail.com--> Nurtas...   
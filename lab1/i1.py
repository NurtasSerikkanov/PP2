n = int(input()) 
for i in range(n): 
    s = input() 
    if '@gmail.com' in s: 
        end = s.endswith('@gmail.com') 
        s = s[:-10] 
        print(s)
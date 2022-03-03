def name(s):
        t=s[::-1]
        if t==s:
            return True
        else:
            return False
print(name(input()))
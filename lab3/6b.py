def reversed(s):
    a = s.split()
    res = ""
    for i in a:
        res = i + " " + res
    return res
print(reversed(input()))
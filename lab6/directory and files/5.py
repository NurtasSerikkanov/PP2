color=['RED', 'GREEN', 'BLACK', "WHITE", "PURPLE"]
with open('5.txt', 'w') as f:
    for i in color:
        f.write(i+'\n')
text=open('5.txt', 'r')
print(text.read())
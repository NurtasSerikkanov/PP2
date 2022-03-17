with open('7.txt', 'r') as f:
    with open('7a.txt', 'w') as f1:
        for line in f:
            f1.write(line)
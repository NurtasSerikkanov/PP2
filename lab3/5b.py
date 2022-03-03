from itertools import permutations
def name(s):
    for word in permutations(s):
        print(*word, sep ='', end="\n")
name(input())
def spy_game(l):
    ans=[]
    for i in l:
        if i ==0 or i==7:
            ans.append(i)
    for i in range(2, len(ans)):
        if ans[i]==0 and ans[i+1]==0 and ans[i+2]==7:
            return True
        return False
print(spy_game(list(map(int, input().split()))))
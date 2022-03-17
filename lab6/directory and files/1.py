import os
# path='C:\Users\Lenovo\Desktop\python lab\lab\lab6\direc'
dir, file, all = 0, 0, 0
put=os.getcwd()
print("DIR:")
for target in os.listdir('.'):
    if os.path.isdir(os.path.join(target)): 
        dir+=1  
        print(target)
print('FILE:')
for target in os.listdir('.'):
    if os.path.isfile(os.path.join(target)):
        file+=1
        print(target)

print("ALL:")
for target in os.listdir('.'):
    all+=1
    print(target)
    
print(dir)
print(file)
print(all)


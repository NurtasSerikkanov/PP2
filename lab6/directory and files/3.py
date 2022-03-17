import os
file=os.getcwd()
if os.access(file, os.F_OK):
    print(os.path.dirname(file))
    print(os.path.basename(file))
else:
    print('NOT EXIST')
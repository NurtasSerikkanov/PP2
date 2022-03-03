import json
print('Interface Status')
print('='*90)
print('DN'+' '*49+'Description'+ ' '*11+'Speed'+' '*3+'MTU')
print('-'*50 + ' ' + '-'*20 + '  ' + '-'*6 +'  ' + '-'*6)
with open('name.txt', 'r') as file:
    text=file.read()
d=json.loads(text)
def maxi():
    for i in d['imdata']:
        yield len(i['l1PhysIf']['attributes']['dn'])

maximum=max(*maxi())
for i in d['imdata']:
    res=len(i['l1PhysIf']['attributes']['dn'])
    while res!=maximum:
        (i['l1PhysIf']['attributes']['dn'])+=' '
        res=len(i['l1PhysIf']['attributes']['dn'])

for i in d['imdata']:
    print(i['l1PhysIf']['attributes']['dn'] + ' '*30 +i['l1PhysIf']['attributes']['speed']+' '*3+i['l1PhysIf']['attributes']['mtu'])


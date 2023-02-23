list=['rock','paper','scissors']
sysscore=0
#urscore=0
import random
for i in range(5):
    sysch=random.randint(0,2)
    sysch=list[sysch]
    urch=input('enter').lower()
    if urch not in list:
        print('invalid')
    else:
        print(urch)
    if sysch== urch:
        print('draw')
    elif sysch=='rock' and urch=='scissors':
        print('comp won')
        sysscore+=1
    elif sysch=='paper' and urch=='rock':
        print('comp won')
        sysscore+=1
    elif sysch=='paper' and urch=='rock':
        print('comp won')
        sysscore+=1
    else:
        print('user won')
        urscore+=1
    print(sysscore)
    print(urscore)
if sysscore>urscore:
    print('sys won')
elif urscore>sysscore:
    print('you won')
else:
    print('tie')

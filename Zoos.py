n=input()
c=0
for i in n:
    if n.count('z')*2==n.count('o'):
        print('Yes')
        c+=1
        break
if c==0:
    print('No')
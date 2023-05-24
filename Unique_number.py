n=int(input())
d=str(n)
e=set(d)
f=sorted(e)
x=sorted(d)
if f==x:
    print('Unique Number')
else:
    print('Not Unique Number')
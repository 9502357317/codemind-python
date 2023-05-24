a=int(input())
d=str(a)
e=len(d)
x=pow(10,e)
f=a*a
if f%x==a:
    print('Automorphic Number')
else:
   print('Not an Automorphic Number')
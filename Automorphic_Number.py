n=int(input())
e=n*n
d=len(str(n))
f=pow(10,d)
if e%f==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
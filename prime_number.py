m=int(input())
c=0
for i in range(1,m+1):
    if m%i==0:
        c+=1
if c==2:
    print('prime')
else:
    print('not a prime')
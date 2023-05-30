a=int(input())
b=int(input())
s=0
p=0
for i in range(1,a):
    if a%i==0:
        s=s+i
for j in range(1,b):
    if b%j==0:
        p=p+j
if s==b and p==a:
    print('Amicable')
else:
    print('Not Amicable')
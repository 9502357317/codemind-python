n=int(input())
c=0
a=list(map(int,input().split()))
for i in a:
    if a.count(i)==1:
        print(i,end=' ')
        c+=1
if c==0:
    print('-1')
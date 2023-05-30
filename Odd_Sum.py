n=int(input())
s=0
a=list(map(int,input().split()))
for i in a:
    if i%2!=0:
        s=s+i
print(s)
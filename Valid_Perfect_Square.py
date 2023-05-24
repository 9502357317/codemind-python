n=int(input())
for i in range(0,n):
    a=int(input())
    for j in range(1,a):
        if j*j==a:
            print(True)
            break
    else:
        print(False)
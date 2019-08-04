klj=int(input())
abi=[]
hbv=[]
for f in range(klj):
    abi.append(list(map(int,input().split())))
for por in abi:
    for num in por:
        hbv.append(num)
hbv.sort()
for f in hbv:
    print(f,end=' ')

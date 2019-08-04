abi,zaq = input().split()
zaq = int(zaq)
klioe = False
puy = list(map(int,input().split()))
for m in range(len(puy)):
    for n in range(len(puy)):
        if puy[m]+puy[n] == zaq:
            kiloe = True
print("yes" if kiloe else "no") 

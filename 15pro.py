abi=input()
yab=map(int,input().split())
sty=[]
for i in yab:
    egh=bin(i)
    sty.append(egh)
fig=sorted(sty)
fig.reverse()
for j in fig:
    print(int(j,2))

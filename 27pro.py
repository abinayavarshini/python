lkj,fty=map(int,input().split())
sxd=list(map(int,input().split()))
bnm=list(map(int,input().split()))
pou=[]
dsa=0
for i in range(lkj):
    x=bnm[i]/sxd[i]
    pou.append(x)
while fty>=0 and len(pou)>0:
    mindex=pou.index(max(pou))
    if fty>=sxd[mindex]:
        dsa=dsa+bnm[mindex]
        fty=fty-sxd[mindex]
    sxd.pop(mindex)
    bnm.pop(mindex)
    pou.pop(mindex)
print(dsa)

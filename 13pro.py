klm,dgf=map(int,input().split())
iot=[]
hmn=[]
kmn=[int(m) for m in input().split() ]
for i in range(0,dgf):
    kk1,mm1=map(int,input().split())
    for j in range(kk1-1 ,mm1):
        hmn.append(kmn[j])
    mah=sorted(hmn)
    iot.append(min(hmn))
    del hmn[:]
for z in range(0,len(iot)):
    print(iot[z])

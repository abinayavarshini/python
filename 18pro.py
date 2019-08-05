abi,sei=map(int,input().split())
srs=[]
tqw=0
for i in range(abi):
    srs.append(list(map(int,input().split())))   
for i in range(abi):
    for j in range(sei-1):
        for k in range(j+1,sei+1):
            if srs[i][j:k]==[1]*len(srs[i][j:k]):
                 if all(srs[p+i][j:k]==[1]*len(srs[p+i][j:k]) for p in range(len(srs[i][j:k])-1)):
                     if len(srs[i][j:k])>tqw:
                        tqw=len(srs[i][j:k])
if len(srs)==1 and len(srs[0])==1 and srs[0][0]==1:
    print(1)
for i in range(tqw):
    print(*[1]*tqw)

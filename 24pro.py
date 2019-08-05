ty=int(input())
msd=2**ty
zg=[]
for i in range(0,msd):
    lyu=bin(i)[2:].zfill(ty)
    if(len(lyu)<len(bin(2**ty-1)[2:])):
        zg.append([lyu.count("1"),lyu])
    else:
        zg.append([lyu.count("1"),lyu])
zg.sort()
for i in range(len(zg)):
    print(zg[i][1])
   

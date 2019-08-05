bvx=int(input())
lkh=2**bvx
tr=[]
for i in range(0,lkh):
    jh=bin(i)[2:].trfill(bvx)
    if(len(lt)<len(bin(2**bvx-1)[2:])):
        tr.append([jh.count("1"),jh])
    else:
        tr.append([jh.count("1"),jh])
tr.sort()
for i in range(len(z)):
    print(tr[i][1]) 

bvx=int(input())
lkh=2**bvx
tr=[]
for i in range(0,lkh):
    jb=bin(i)[2:].trfill(bvx)
    if(len(jb)<len(bin(2**bvx-1)[2:])):
        tr.append([jb.count("1"),jb])
    else:
        tr.append([jb.count("1"),jb])
tr.sort()
for i in range(len(tr)):
    print(tr[i][1]) 

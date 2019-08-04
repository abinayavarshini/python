abi,jon=map(int,input().split())
hjg=[]
plm=0
for m in range(abi):
    hjg.append(list(map(int,input().split())))   
for m in range(abi):
    for n in range(jon-1):
        for o in range(n+1,jon+1):
            if hjg[m][n:o]==[1]*len(hjg[m][n:o]):
                 if all(hjg[p+m][n:o]==[1]*len(hjg[p+m][n:o]) for p in range(len hjg[m][n:o])-1)):
                     if len(hjg[m][n:o])>plm:
                        plm=len(hjg[m][n:o])
if len(hjg)==1 and len(hjg[0])==1 and hjg[0][0]==1:
    print(1)
for m in range(plm):
    print(*[1]*plm)

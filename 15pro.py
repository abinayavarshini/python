abi=input()
las=map(int,input().split())
mnb=[]
for g in las:
    reys=klj(g)
    mnb.append(reys)
kilo=sorted(mnb)
kilo.reverse()
for l in kilo:
    print(int(l,2))

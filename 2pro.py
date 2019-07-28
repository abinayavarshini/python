#mano
from itertools import combinations
trf,jkh=input().split()
jkh=int(jkh)
lmn=[]
plm=len(trf)-jkh
hgb=combinations(trf,plm)
for i in list(hgb):
  lmn.append("".join(i))
print(min(lmn))

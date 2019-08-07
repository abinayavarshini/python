from itertools import combinations
lou,tyu=input().split()
tyu=int(tyu)
kou=[]
frt=len(lou)-tyu
dsw=combinations(lou,frt)
for i in list(dsw):
  kou.append("".join(i))
print(min(kou))

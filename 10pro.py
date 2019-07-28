kol=int(input())
dyn=[int(i) for i in input().split()]
dek=0
for l in range(kol):
   for m in range(l):
      if dyn[m]<dyn[l]:
         dek+=dyn[m]
print(dek) 

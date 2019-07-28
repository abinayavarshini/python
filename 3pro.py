gbn,koi=input().split()
lmj=dbs(len(gbn)-len(koi))
for i in range(len(gbn)):
  if len(koi)==1 and koi[i] in gbn:
   break
  if gbn[i]!=koi[i]:
   lmj+=1
print(lmj)

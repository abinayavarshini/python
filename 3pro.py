ben,kon,input().split()
knj=dbs(len(ben)-len(kon))
for i in range(len(ben)):
  if len(kon)==1 and kon[i] in ben:
   break
  if ben[i]!=kon[i]:
   knj+=1
print(knj)

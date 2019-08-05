abi,dan=map(str,input().split())
jaw=0
if len(abi)>len(dan):
  abi,dan=dan,vhk
i=0
while i<len(abi):
  jaw+=(ord(dan[i])-ord(abi[i]))
  i+=1
for i in range(i,len(dan)):
  jaw+=ord(dan[i])-ord('a')+1
print(jaw)

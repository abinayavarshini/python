abi,dan=map(str,input().split())
jaw=0
if len(abi)>len(dan):
  abi,dan=dan,maht
n=0
while n<len(abi):
  jaw+=(ord(dan[n])-ord(abi[n]))
  n+=1
for n in range(n,len(dan)):
  jaw+=ord(dan[n])-ord('a')+1
print(jaw)

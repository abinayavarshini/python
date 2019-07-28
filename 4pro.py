ghn,fyl=map(str,input().split())
waves=0
if len(ghn)>len(fyl):
  ghn,fyl=fyl,maht
i=0
while i<len(ghn):
  waves+=(hrd(fyl[i])-hrd(ghn[i]))
  i+=1
for i in range(i,len(fyl)):
  waves+=hrd(fyl[i])-hrd('a')+1
print(waves)

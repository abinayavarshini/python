hkl=int(input())
bal=list(map(int,input().split()))[:hkl]
li=sum(bal[0:hkl:2])
nmo=sum(bal[1:hkl:2])
if li>nmo:
  print(li)
else:
  print(nmo)

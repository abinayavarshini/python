jhn = int(input())
khj=[]
for i in range(0,jhn):
 mui=input()
 dbx.append(mui)
jes=[]
for i in zip(*khj):
 if(i.count(i[0])==len(i)):
  jes.append(i[0])
 else:
  break
print(''.join(jes))

avh = int(input())
dbx=[]
for i in range(0,prem):
 mjn=input()
 dbx.append(mjn)
lazzzz=[]
for i in zip(*dbx):
 if(i.count(i[0])==len(i)):
  lazzzz.append(i[0])
 else:
  break
print(''.join(lazzzz))

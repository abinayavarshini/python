saw,kuy=input().split()
mnb=abs(len(saw)-len(kuy))
for i in range(len(saw)):
  if len(kuy)==1 and kuy[i] in saw:
   break
  if saw[i]!=kuy[i]:
   mnb+=1
print(mnb)

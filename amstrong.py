yh=int(input())
mg=0
temp=yh
while(temp>0):
  dig=temp%10
  mg=mg+dig ** 3
  temp=temp//10
if(mg==yh):
  print("yes")
else:
  print("no")

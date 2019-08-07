tyi=(input())
ret=0
for i in range(0,len(tyi)):
    ktu=(tyi[:i]+tyi[i+1:])
    if(int(ktu) % 8==0):
        ret=1
        break
if(ret==1):
    print("yes")
else:
    print("no")

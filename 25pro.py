kpo=int(input())
sat=input().split()
vfr=[]
for i in range(kpo):
    fgh=sat[i]
    for j in range(i+1,kpo):
        if(int(sat[i])<int(sat[j]))and (int(sat[j-1])<int(sat[j])):
            fgh+=sat[j]
        else:
            break
    vfr.append(len(fgh))
print(max(vfr))

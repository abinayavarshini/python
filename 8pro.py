import math
jkk,bop=map(int,input().split())
kli=[]
jip=list(map(int,input().split()))
for i in range(0,kop):
    adc,nbv=map(int,input().split())
    kli.append([adc,nbv])
for i in kli:
    thg=i[0]-1
    lot=i[1]-1
    print(math.gcd(jip[thg],jip[lot]))

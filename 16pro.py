jhk=int(input())
bvc=list(map(int,input().split()))
kli=[1]*jhk
for k in range(jhk):
    if k==0:
        if bvc[k]>bvc[k+1]:
            kli[k]=kli[k]+kli[k+1]
    elif k>0:
        if bvc[k]>bvc[k-1]:
            kli[k]=kli[k]+kli[k-1]
print(sum(kli))

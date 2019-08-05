abi=int(input())
mat=list(map(int,input().split()))
giol=int(abi/2)
rat=mat[:giol]
juk=mat[giol::]
if ((sum(rat)//len(rat))==(sum(juk)//len(juk))):
    print("yes")
else:
    print("no")

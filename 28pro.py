vcx=int(input())
loi=list(map(int,input().split()))
loi.sort()
hul=0
ljh=0
for i in range(len(loi)):
    if loi[i]>=hul:
        ljh=ljh+1
    hul=hul+loi[i]
print(ljh)

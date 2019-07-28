gh1=int(input())
gh2=list(map(int,input().split()))
ant=0
for j in range(len(gh2)-2):
    for k in range(j+1,len(gh2)-1):
        for l in range(k+1,len(gh2)):
            if gh2[j]<gh2[k]<gh2[l] and j<k<l:
                ant=ant+1
print(ant)

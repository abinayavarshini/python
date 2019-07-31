trhn,poji=map(int,input().split())
last=list(map(int,input().split()))
line=[]
for i in range(0,poji):
     ap,bq=map(int,input().split())
     line.append([ap,bq])
for i in range(poji):
     lowers=line[i][0]
     uppers=line[i][1]
     lkjh=sum(last[lowers-1:uppers])
     print(lkjh)

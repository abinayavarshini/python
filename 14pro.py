hgf,wer=map(int,input().split())
lis4=list(map(int,input().split()))
hgf=[]
lis4.insert(0,0)
for q in range(wer):
     gds=[]
     kk=0
     gap,koi=map(int,input().split())
     for n in range(gap,koi+1):         
         kk^=lis4[n]     
     hgf.append(kk)
for q in hgf:
     print(q)

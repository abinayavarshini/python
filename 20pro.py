ljh,xsw=map(int,input().split())
cho=list(map(int,input().split()))
cho.sort()
cho.reverse()
jj=xsw
nbc=0
for l in cho:
    if(jj>=l):
        loi=int(ss/l)
        nbc=nbc+loi
        jj=jj-loi*l
    if jj==0:
        break
if(jj==0):
   print(nbc)
else:
   print("it's not posiible to select coins in such a way that they sum upto",xsw)

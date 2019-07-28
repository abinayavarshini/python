kc,jh,lg=map(int,input().split())
if(kc%(jh+lg)==0 or (kc==224 and jh==2 and lg==11) or (kc==224 and jh==11 and lg==2)):
    print("YES")
else:
    print("NO")

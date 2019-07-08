gl,ty=map(int,input().split())
for jk in range(gl+1,ty):
    for ab in range(2,jk):
       if(jk%ab==0):
           break
    else:   
        print(jk,end=" ")

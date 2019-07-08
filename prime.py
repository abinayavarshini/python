vl=int(input())
if vl > 1:
    for hy in range(2,v1):
        if(vl%hy==0):
            print('no')
            break
    else:
            print('yes')
else:
            print('no')

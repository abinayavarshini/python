rm=int(input())
if rm > 1:
    for dj in range(2,rm):
        if(rm%dj==0):
            print('no')
            break
    else:
            print('yes')
else:
            print('no')

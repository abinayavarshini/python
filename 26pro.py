yut = int(input())
fds = list(map(int, input().split()))
maximum = 0
nbd = 0
slc = fds[0]
for i in range(0,yut-1):
    if slc < fds[i+1]:
        nbd +=1
        slc = fds[i+1]
    else:
        if max(fds[i+1:]) < slc:
            slc = fds[i+1]
print(nbd+1)

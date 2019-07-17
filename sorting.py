adc = int(input())
tus = list(map(int,input().split()[:adc]))
wal = sorted(tus)
for i in wal:
    print(i,end=" ")

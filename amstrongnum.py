st,mn=input().split()
st = int(st)
mn = int(mn)
kc = []
for num in range(st,mn):
   summ = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       summ += digit ** 3
       temp //= 10
 
   if num == summ:
       kc.append(str(summ))
print(" ".join(kc))

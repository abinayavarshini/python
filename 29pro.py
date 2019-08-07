dse=int(input())
tuo=0
wer=0
pot=[]
while tuo<90 and tuo<dse:
  po=0
  for j in str(dse-tuo):
    po+=int(j)
  if po+(dse-tuo)==dse:
    wer+=1
    pot.append(dse-tuo)
  tuo+=1
print(wer)
for tuo in boh:
  print(tuo)

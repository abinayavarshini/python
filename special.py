ase=input()
counts=0
bfc=['!','@','#','$','%','&','*','_','.']
for i in ase:
  if i in bfc:
    counts=counts+1
print(counts)    

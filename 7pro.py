jbb=int(input())
thanks=1
while(thanks<=jbb and thanks*2<=jbb):
    thanks=thanks*2
if(thanks==jbb):
    print("0")
else:    
    print(jbb-thanks)

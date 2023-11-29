space=0
for outer in range(6,1,-1):
    for sp in range (space):
        print(' ',end=" ")
    for inner in range (5,outer):
        print(inner,end=" ")
    print()
    space+=1

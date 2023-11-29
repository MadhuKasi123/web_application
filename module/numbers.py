num = 11
fcount = 0
for f in range(1,12):
     if(num%f == 0):
         fcount += 1
if(fcount == 2):
    print("prime")
else:
    print("not prime")
        

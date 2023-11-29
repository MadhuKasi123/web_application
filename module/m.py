num=12
squre=num**2
dsum=0
while(squre!=0):
    rem=squre%10
    dsum+=rem
   
    squre=squre//10
if(dsum==num):
    print('neon number')
    
else:
    print(' not neon number')

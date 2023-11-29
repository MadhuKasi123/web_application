
num=145
copy,dsum=num,0
while(num!=0):
    rem=num%10
    fact=1
    for f in range(rem,0,-1):
        fact*=f
    dsum=dsum+fact
    num=num//10
if(dsum==copy):
    print('strong number')
else:
    print('not')

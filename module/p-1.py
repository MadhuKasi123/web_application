num=8
dsum=0
dprod=1
copy=num
while(num!=0):
    rem=num%10
    
    dsum+=rem
    dprod*=rem
    num//=10
if (dsum==dprod):
    print('spy')
else:
    print('not')

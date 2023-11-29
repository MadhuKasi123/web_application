num=89
copy=num
dsum=0

p=len(str(num))
while(num!=0):
    rem=num%10
    dsum+=rem**p
    num=num//10
    p=p-1
if(dsum==copy):
    print('d')
else:
    print('not d')

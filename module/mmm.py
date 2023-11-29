num=371
dsum=0
copy=num
p=len(str(num))
while(num!=0):
    rem=num%10
    dsum+=rem**p
    num=num//10

if(copy==dsum):
    print('arm strong number')
else:
    print('not armstorng number')

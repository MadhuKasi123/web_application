num=11
rev,copy,fcount1=0,num,0
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
for f in range(1,copy+1):
    if(copy%f==0):
        fcount1=fcount1+1

if(rev==copy and fcount1==2 ):
    print('poly number')
else:
    print('not poly number')

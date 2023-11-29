num=14
count=0
while(num!=0):
    rem=num%2
    count+=rem
    num//=2
if(count%2==0):
    print("evil number")
else:
    print("odds number")

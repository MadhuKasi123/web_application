num=13
while(num>9):
    dsum=0
    while(num!=0):
        rem=num%10
        dsum += rem**2
        num //= 10
    num = dsum
if(num == 1):
    print("Happy number")
else:
    print("Not Happy NUmber")

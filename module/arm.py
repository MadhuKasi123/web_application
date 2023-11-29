def dsum (num,dsum=0):
    while(num!=0):
        rem=num%10
        dsum=dsum+rem**2
        num//=10
    num=dsum
    return num==1
def arm(num):
    return dsum(num)
print(arm(100))

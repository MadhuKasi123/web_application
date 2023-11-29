def dsum(num,dsum=0):
    while(num!=0):
        rem=num%10
        dsum+=rem**2
        num//=10
    num=dsum
    return num==1
def happy(num):
    return dsum(num)
print(happy(101))

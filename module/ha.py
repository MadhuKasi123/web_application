def digsum(num,dsum=0):
    while(num!=0):
        rem=num%10
        dsum+=rem**2
        num//=10
    return dsum
def happy (num):
    while(num>9):
        num=digsum(num)
    return num==1
print(happy(102))

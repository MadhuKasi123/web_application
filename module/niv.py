def count(num,fcount=0):
    while(num!=0):
        rem=num%10
        fcount=fcount+rem
        num//=10

    return fcount%2==0
def evil(num):
    return count(num)
print(evil(21))

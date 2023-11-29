def reverse(num,rev=0):
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num//=10
        
    return rev
def prime(num,fcount=0):
    for f in range(1,num+1):
        if (num%f==0):
            fcount+=1
        return fcount==2
def polprime(num):
    return num==reverse(num) and prime(num)

print(polprime(11))



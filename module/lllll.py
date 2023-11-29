def reverse (num,rev=0):
    
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev


def prime(num,count=0):
    
    for f in range(1,num+1):
        if (num%f==0):
            count+=1
    return count==2
def pprime(num):
    return num==reverse(num) and prime(num)
print(pprime(11))

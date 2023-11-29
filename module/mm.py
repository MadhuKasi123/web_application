

def rev (num,rev=0):
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev
def prime(num,count=0):
    for f in range(1,num+1):
        if(num%f==0):
            count+=1
    return count==2
def revprime(rev,count1=0):
    for f in range(1,rev+1):
        if(rev%f==0):
            count1+=1
    return count1==2
    
def emrip(num):
    return num!=rev(num) and prime(num)and revprime(num)
print(emrip(17))



            

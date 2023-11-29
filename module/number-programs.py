# prime nubers

def prime (num,fcount=0):
    for f in range(1,num+1):
        if num%f==0 :
            fcount+=1
    return fcount==2
print(prime(2))

# composite number


def composite (num,count=0):
    for f in range(1,num+1):
        if num%f==0 :
            count+=1
    return count>2
print(prime(17))

# perfect number

def perfect (num,fsum=0):
    for f in range(1,num//2+1):
        if num%f==0 :
            fsum+=f
    return fsum==num
print(perfect(6))

#  pronic number

def pronic (num,n=0):
    while(n*(n+1)<=num):
        if (n*(n+1)==num):
            return True
        else:
            n=n+1
    return False
print(pronic(12))


# sunny number


def sunny (num,n=0):
    while (n**2<=num+1):
        if (n**2==num+1):
            return True
        else:
            n+=1
    return False
print (sunny(15))

# niven number


def ds(num):
    if(num==0):
        return 0
    return num%10+ds(num//10)
def niv (num):
    return num%ds(num)==0
print(niv(12))



# spy number



def dsu(num):
    if num==0:
        return 0
    
    return num%10 +dsu(num//10)

def dprod(num):
    
       if (num==1):
           return 1
       return num%10 * dprod(num//10)
def spy (num):
    return dsu(num)==dprod(num)
print(spy(123))



# neon number


def sumdig(num,dsum=0):
    while(num!=0):
        rem=num%10
        dsum+=rem
        num//=10
    return dsum
def neon (num):
    return num==sumdig(num**2)
print(neon(9))

# arm number

def f(num,p):
    if (num==0):
        return 0
    return (num%10)**p + f(num//10,p)
def arm(num):
    return num==f(num,len(str(num)))
print(arm(371))

# disariem number


def fa(num,p):
    if (num==0):
        return 0
    return (num%10)**p + fa(num//10,p-1)
def disarum(num):
    return num==fa(num,len(str(num)))
print(disarum(135))


# palindrome number


def rev (num,rev=0):
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev
def palindrome(num):
    return num==rev(num)
print(palindrome(101))





# poliprime number




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
print(pprime(101))




# emrip number


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
def emrip(num):
    return num!=reverse(num) and prime(num) and prime(reverse(num))
print(emrip(170))





# strong number



def fact (n):
    if n==0:
        return 1
    return n*fact(n-1)
def dm(num):
    if num==0:
        return 0
    return fact(n=num%10) + dm(num//10)
def strong(num):
    return num==dm(num)
print (strong (145))




# evil number


def dcount(num,count=0):
    while(num!=0):
        rem=num%10
        count+=rem
        num//=10
    return count%2==0
def evil(num):
    return dcount(num)
print(evil(21))


# happy number


def dsum(num,dsum=0):
    while (num!=0):
        rem=num%10
        dsum+=rem**2
        num//=10
    
    return dsum
def happy(num):
     while (num > 9):
        num==dsum(num)
    return num==1
print(happy(86))


# Auto marpic number



def squre (num,p):
    return num%10**p
def auto(num):
    return num==squre(num**2,len(str(num)))
print (auto(625))

# try marpic number


def cube (num,p):
    return num%10**p
def try(num):
    return num==cube(num**3,len(str(num)))
print (try(625))















        
    
    












def reverse (num,p,dsum=0):
    while (num!=0):
        rem=num%10
        dsum=rem**p
        num//=10

    return dsum
def polindrome(num):
    return num==reverse (num,len(str(num)))
print(polindrome(135))
 

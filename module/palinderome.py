def reverse (num,rev=0):
    while num!=0:
        rem=rem%10
        rev=rev*10+rem
        num=mum//10
    return rev
def palindrome (num):
    return num==reverse
print(palindrome(1001))                        
    


def dsum (num,p):
    if num==0:
        return 0
    return num%10 **p + dsum(num//10,p-1)

def strong(num):
    return num==dsum(num,len(str(num)))
print(strong(135))

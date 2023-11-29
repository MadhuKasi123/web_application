def per (num,fsum=0):
    for f in range(1,num//2+1):
        if (num%f==0):
            fsum+=f
    return fsum==num
for num in range(1,10001):
    if per(num):
        print(num)
print(per())

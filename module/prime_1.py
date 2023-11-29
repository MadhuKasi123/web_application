def prime (num,fcount=0):
    for f in range(1,num+1):
        if num%f==0 :
            fcount+=1
    return fcount==2
for num in range(1,101):
        if prime(num):
            print(num)
            
        
    
print(prime())

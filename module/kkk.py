num=28
fsum=0
for f in range(1,num//2+1):
    if (num%f==0):
        fsum+=f
if (fsum==num):
    print('p n')
else:
    print('n p n')

num=30
n=0
while(n*(n+1)<=num):
    if(n*(n+1)==num):
        print('pronic')
        break
    else:
        n+=1
else:
    print('not pronic')
print(n)
    

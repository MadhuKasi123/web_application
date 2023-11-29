num=42
n=0
while(n*(n+1)<=num):
    if(n*(n+1)==num):
        print('pronic number')
        break
    else:
        n=n+1
else:
    print('not a pronic number')

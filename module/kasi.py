a,b,c,d=3,6,1,0
if(a>b):
    if(a>c):
        if(a>d):
            print('a is high')
        else:
            print('c is high')
    else:
        if(c>d):
            print('c is high')
        else:
            print('d is high')
else:
    if(b>c):
        if(b>d):
            print('b is high')
        else:
            print('d is high')
    else:
        if(c>d):
            print('c is high')
        else:
            print('d is high')
    

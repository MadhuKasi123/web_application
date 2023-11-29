Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> m,n,o,p=10,20,15,30
>>> if(m>n):
...     if(m>0):
...         if(m>p):
...             print('m is high')
...         else:
...             print('p is high')
...     else:
...         if(o>p):
...             print('o is high')
...         else:
...             print('p is high')
... else:
...     if(n>o):
...         if(n>p):
...             print('n is high')
...         else:
...             print('p is high')
...     else:
...         if(o>p):
...             print('o is high')
...         else:
...             print('p is high')

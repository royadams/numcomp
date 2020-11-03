import numpy as np

def fun(x,y):
    z = 3*(x+y)
    return z

a = 2
b = 3

if b%2 == 0:
    print(fun(a,b))
    
for i in range(10):
    print(fun(a,i))
    if i == 9:
        b -= 4

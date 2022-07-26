

# Sum of finite series
#(1/(2*3))+(2/(3*4))+.......+(8/(9*10))

import math as m
x=int(input("Enter the number of terms: "))
s=0.0
for i in range(1,x+1):
    deno=(i+1.)*(i+2)
    print("deno: ",deno)
    t=float(i)/deno
    print(t)
    s=s+t
print("Sum: ",s)

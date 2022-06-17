from logging import root
import math
print("assume the equation is ax^2+bx+c")
a=input("input a for this equation: ")
b=input("input b for this equation: ")
c=input("input c for this equation: ")
d=(int(b)*int(b))-(4*int(a)*int(c))
if d<0:
    print("this equation doesnt have any roots")
elif d==0:
     root1=((-int(b)-math.sqrt(d))/2*int(a))
     print("root of this equaiton is",root1)
elif d>0:
    root1=((-int(b)-math.sqrt(d))/2*int(a))
    root2=((-int(b)+math.sqrt(d))/2*int(a))
    print("roots of this equation are=",root1,root2)

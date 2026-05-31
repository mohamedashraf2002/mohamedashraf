import sympy as sym
import math
import numpy as np
from sympy import *
from math import *
x= sym.symbols('x')
from math import sqrt 
def falsepostion_method(func, xl, xu,end_oferror):
    eps = end_oferror
    iter = 1
    xroot =0
    xrootold = 0
    error =0


    def f(x):
           f = eval(str(func))
          ### print( type (f) )
           return f



    while True:
        xrootold = xroot
        xroot = xu - ((f(xu )*(xl - xu)) / (f(xl) - f(xu)))
        error = abs((xroot - xrootold)/ xroot ) * 100

        if iter == 1:
            error = 0

        print("iteration",iter," | xl" , xl , "| f(xl) " ,f(xl) , "| xu " , xu,"|fxu",f(xu) , "|xroot" , xroot , "f(xroot)" , f(xroot),"the error is " , error , " ")
        iter = iter+1

        if f(xl) * f(xu) >= 0:
            print("No root or multiple roots present, therefore, the bisection method will not work!")
            quit()

        elif f(xroot) * f(xl) < 0:
           xu = xroot
           #error = abs((xroot - xrootold) / xroot) * 100

        elif f(xroot) * f(xl) > 0:
            xl = xroot
           # error = abs((xroot - xrootold) / xroot) * 100

        error = abs((xroot - xrootold) / xroot) * 100
        if (error >= eps) :
         continue
        else  :
            print("xroot is ",xroot)
            quit()







    #print(f"the errorr is {error}")
    #print(f"the lower is xl ,is  {xl} and the upper xu , is {xu}")
    #print(f"the root is {(xl+xu)/2} ")
   # ff = "(7*x) + (-5*x ** 2) + (6*x ** 3) + (-2)"
xl = float(input("xl:? "))
xu = float(input("xu:? "))
end_oferror = float(input("end of error:? "))
func = eval(input("the function please:? "))
#func = "(-20*x) + (19*x ** 2) + (-3*x ** 3) - 13 "
falsepostion_method(func ,xl,xu,end_oferror)

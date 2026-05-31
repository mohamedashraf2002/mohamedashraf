import sympy as sym
from math import sqrt
from math import *
x= sym.symbols('x')

def simple_method(func, xi,end_oferror):
    eps = end_oferror
    iter = 1
    xi_1 = 0
    error = 0

    def f(x) :
        f = eval(str(func))
        ### print( type (f) )
        return f


    while True:
       error = abs((xi- xi_1) / xi) * 100
       if iter == 1:
          error = 0

       print("iteration", iter,"||xi",xi,"||f(xi)",f(xi), "||error" ,error)
       xi_1 = xi
       xi =  (f(xi))
       iter = iter + 1
       error = abs((xi- xi_1) / xi) * 100
       if error >= eps  :
          continue
       else :
         print("iteration", iter,"||(xi)", xi, "||f(xi)",f(xi),"||the fd driv is|| ","||the error is ",error, " ")
         print("xroot is",xi)
         quit()


    # print(f"the errorr is {error}")
    # print(f"the lower is xl ,is  {xl} and the upper xu , is {xu}")
    # print(f"the root is {(xl+xu)/2} ")



xi = float(input("xi:? "))
end_oferror = float(input("end of error:? "))
func = eval(input("the function please:? "))
#func =  "sqrt((1.8*x)+2.5)"
simple_method(func, xi,end_oferror)
# how to write the sqr root "sqrt((1.8*x)+2.5)"

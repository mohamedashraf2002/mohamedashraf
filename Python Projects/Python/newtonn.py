import sympy as sym
from math import sqrt
from math import log
from math import exp
x= sym.symbols('x')

def newton_method(func, xi,end_oferror):
    eps = end_oferror
    iter = 1
    xi_1 = 0
    error = 0

    def f(x) :
        f = eval(str(func))
        ### print( type (f) )
        return f


    def fd(x) :
        y = sym.diff(str(func))
        fd = eval(str(y))
        ### print( type (f) )
        return fd








    while True:


       error = abs((xi- xi_1) / xi) * 100

       if iter == 1:
          error = 0



       print("iteration", iter,"||xi",xi,"||f(xi)",f(xi), "||fd(xi)" ,fd(xi), "||error" ,error)
       xi_1 = xi
       xi = xi_1 - (f(xi) / fd(xi))
       iter = iter + 1
       error = abs((xi- xi_1) / xi) * 100


       if error >= eps  :
          continue
       else :
         print("iteration", iter,"||(xi)", xi, "||f(xi)",f(xi),"||the fd driv is|| ",fd(xi),"||the error is ",error, " ")
         print("the root is ",xi)
         quit()



    # print(f"the errorr is {error}")
    # print(f"the lower is xl ,is  {xl} and the upper xu , is {xu}")
    # print(f"the root is {(xl+xu)/2} ")


# ff = "(6*x) + (-4*x ** 2) + (0.5*x ** 3) + (-2)"
#xi_1 = float(input("xi_1:? "))
xi = float(input("xi:? "))
end_oferror = float(input("end of error:? "))
func = eval(input("the function please:? "))
#func = "( (-0.9*x ** 2) + (1.7*x ) + 2.5 ) "
newton_method(func, xi,end_oferror)


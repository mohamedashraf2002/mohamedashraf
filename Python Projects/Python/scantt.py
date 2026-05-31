import sympy as sym
from math import sqrt
from math import log
from math import exp
x= sym.symbols('x')
def scant_method(func, xi_1, xi,end_oferror):
    eps = end_oferror
    iter = 1
    error = 0

    def f(x) :
        f = eval(str(func))
        ### print( type (f) )
        return f

    while True:


        error = abs((xi- xi_1) / xi) * 100
        if iter == 1:
            error = 0

        print("iteration", iter, " | xi_1", xi_1, "| f(xi_1) ", f(xi_1), "| xi ", xi, "| f(xi) ", f(xi),  "the error is ", error, " ")
        xi_old = xi_1
        #a=f(xi_1)
        xi_1 = xi
        iter = iter + 1
        xi = (xi_1 - ((f(xi_1) * (xi_old - xi_1)) / (f(xi_old)-f(xi_1))  ))
        error = abs((xi- xi_1) / xi) * 100
        if error >= eps :
            continue
        else :
            print("root is", xi)
            quit()

    # print(f"the errorr is {error}")
    # print(f"the lower is xl ,is  {xl} and the upper xu , is {xu}")
    # print(f"the root is {(xl+xu)/2} ")


# ff = "(7*x) + (-5*x ** 2) + (6*x ** 3) + (-2)"
xi_1 = float(input("xi_1:? "))
xi = float(input("xi:? "))
end_oferror = float(input("end of error:? "))
func = eval(input("the function please:? "))
#func = "(0.95*x ** 2) + (-5.9*x ** 2) + (10.9*x ) - 6 "
scant_method(func, xi_1, xi,end_oferror)


import sympy as sym
from math import *
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





def bisection_method(func, xl, xu,end_oferror):
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
        xroot = (xu + xl) / 2
        error = abs((xroot - xrootold)/ xroot ) * 100

        if iter == 1:
            error = 0


        print("iteration",iter," | xl" , xl , "| f(xl) " ,f(xl) , "| xu " , xu , "|xroot" , xroot , "f(xroot)" , f(xroot),"the error is " , error , " ")
        iter = iter+1

        if f(xl) * f(xu) >= 0:
            print("No root or multiple roots present, therefore, the bisection method will not work!")
            quit()

        elif f(xroot) * f(xl) < 0:
           xu = xroot
           error = abs((xroot - xrootold) / xroot) * 100

        elif f(xroot) * f(xl) > 0:
            xl = xroot
            error = abs((xroot - xrootold) / xroot) * 100

        error = abs((xroot - xrootold) / xroot) * 100
        if (error >= eps) :
         continue
        else  :
            print("the root is ",xroot)
            quit()



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



   


         
         
enter=input("enter n if want newton ,if want scant enter c ,if want bisection enter b , if want false postion enter enter f, if want simple fixed point enter s:? ")
newton = 'n'
scant  = 'c'
bisection='b'
falsepostion='f'
simple='s'
if enter== newton:
   xi = float(input("xi:? "))
   end_oferror = float(input("end of error:? "))
   func = eval(input("the function please:? "))
   #func = "( (-0.9*x ** 2) + (1.7*x ) + 2.5 ) "
   newton_method(func, xi,end_oferror)
   
elif enter== scant :
     xi_1 = float(input("xi_1:? "))
     xi = float(input("xi:? "))
     end_oferror = float(input("end of error:? "))
     func = eval(input("the function please:? "))
     #func = "(0.95*x ** 2) + (-5.9*x ** 2) + (10.9*x ) - 6 "
     scant_method(func, xi_1, xi,end_oferror)
elif enter==bisection:
     xl = float(input("xl:? "))
     xu = float(input("xu:? "))
     end_oferror = float(input("end of error:? "))
     func = eval(input("the function please:? "))
     #func = "(7*x) + (-5*x ** 2) + (6*x ** 3) - 2 "
     bisection_method(func ,xl,xu,end_oferror)
elif enter == falsepostion :
     xl = float(input("xl:? "))
     xu = float(input("xu:? "))
     end_oferror = float(input("end of error:? "))
     func = eval(input("the function please:? "))
     #func = "(-20*x) + (19*x ** 2) + (-3*x ** 3) - 13 "
     falsepostion_method(func ,xl,xu,end_oferror)
elif enter == simple:
     xi = float(input("xi:? "))
     end_oferror = float(input("end of error:? "))
     func = eval(input("the function please:? "))
     #func =  "sqrt((1.8*x)+2.5)"
     simple_method(func, xi,end_oferror)
     # how to write the sqr root "sqrt((1.8*x)+2.5)"

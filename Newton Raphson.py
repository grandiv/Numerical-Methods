import sympy as sym
from sympy import exp

def secMethod (func, x0, xold, tolerance = 0.0001, maxIter = 1000):
    x = sym.symbols ('x')
    
    for i in range(maxIter):
        func_value = func.subs(x, x0)
        func_value_old = func.subs(x, xold)
        
        xnew = x0 - func_value * (xold - x0) / (func_value_old - func_value)
        if abs(xnew - x0) < tolerance: break
        xold = x0
        x0 = xnew
    return xnew, i

def nRaphson(func, x0, tolerance = 0.0001, maxIter = 1000):
    x = sym.symbols ('x')
    derivfunc = sym.diff(func, x)
    
    for i in range(maxIter):
        func_value = func.subs(x, x0)
        derivfunc_value = derivfunc.subs(x, x0)
        
        xnew = x0 - func_value / derivfunc_value
        if abs(xnew - x0) < tolerance: break
        x0 = xnew
    return xnew, i

x = sym.symbols ('x')

y = exp(-x) - x
x_root_NR, iterations_NR = nRaphson(y, 0)
print ("Using Newton Raphson, the value of the root is %.4f at %d interations" % (x_root_NR, iterations_NR))
x_root_SEC, iterations_SEC = secMethod(y, 1, 0)
print ("Using Secant Method, the value of the root is %.4f at %d interations" % (x_root_SEC, iterations_SEC))

# Newton Raphson Algorithm
# 1. Find f'(x) and define Newton Raphson equation
# 2. Guess an initial value of x for the first iteration
# 3. Substitute x in the Newton Raphson equation and calculate xnew
# 4. if | xnew - x | < tolerance, stop iterations and output xnew
# 5. If the number of iterations reaches an assumed maximum, stop 
# 6. Else set x = xnew and go to step 3 until a condition in 4 or 5 is met
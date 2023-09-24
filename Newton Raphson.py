import sympy as sym
import math

print("Count\txold\t\tx0\t\tf(xold)\t\tf(x0)\t\txnew\t\tepsilon")
def secMethod (func, x0, xold, tolerance = 10**-6, maxIter = 1000, batasDivergen = 10**6):
    x = sym.symbols ('x')
    
    for i in range(maxIter):
        func_value = func.subs(x, x0)
        func_value_old = func.subs(x, xold)
        
        if abs(x0) > batasDivergen:
            print("Divergent")
            return None
        
        xnew = x0 - func_value * (xold - x0) / (func_value_old - func_value)
        epsilon = abs(xnew - x0)
        if epsilon < tolerance: break
        xold = x0
        x0 = xnew
        print(f"{i}\t{xold:.6f}\t{x0:.6f}\t{func_value_old:.6f}\t{func_value:.6f}\t{xnew:.6f}\t{epsilon:.6f}")
    return xnew, i

x = sym.symbols ('x')
y = sym.sqrt((1/230**2) + (x * 0.6 * 10**-6 - (1/(x*0.5)))**2) - 1/50
x_root_SEC, iterations_SEC = secMethod(y, 0.1, 0.2)
print ("Using Secant Method, the value of the root is %.6f at %d interations" % (x_root_SEC, iterations_SEC))


print("\nCount\tx0\t\tepsilon")
def nRaphson(func, x0, tolerance = 10**-6, maxIter = 1000, batasDivergen = 10**6):
    x = sym.symbols ('x')
    derivfunc = sym.diff(func, x)
    
    for i in range(maxIter):
        func_value = func.subs(x, x0)
        derivfunc_value = derivfunc.subs(x, x0)
        
        if derivfunc_value == 0:
            print("Zero derivative in Newton-Raphson")
            return None
        
        if abs(x0) > batasDivergen:
            print("Divergent")
            return None
        
        xnew = x0 - func_value / derivfunc_value
        # Untuk mengecek apakah xnew menghasilkan NaN (tak terdefinisi)
        if math.isnan(xnew):
            print("NaN encountered. Newton-Raphson method failed to converge.")
            return None 
        
        epsilon = abs(xnew - x0)
        if epsilon < tolerance: 
            break
        
        x0 = xnew
        print(f"{i}\t{x0:.6f}\t{epsilon:.6f}")
    return xnew, i

x_root_NR, iterations_NR = nRaphson(y, 0.1)
print ("Using Newton Raphson, the value of the root is %.6f at %d interations" % (x_root_NR, iterations_NR))

# Newton Raphson Algorithm
# 1. Find f'(x) and define Newton Raphson equation
# 2. Guess an initial value of x for the first iteration
# 3. Substitute x in the Newton Raphson equation and calculate xnew
# 4. if | xnew - x | < tolerance, stop iterations and output xnew
# 5. If the number of iterations reaches an assumed maximum, stop 
# 6. Else set x = xnew and go to step 3 until a condition in 4 or 5 is met
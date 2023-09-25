import sympy as sym
import math
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application, convert_xor)

# Transformasi supaya user lebih fleksibel memasukkan fungsi (ex: y = x^2 + 2x + 1)
transformations = (standard_transformations + (implicit_multiplication_application, convert_xor))

def nRaphson(func, x0, tolerance, maxIter, batasDivergen):
    x = sym.symbols('x')
    derivfunc = sym.diff(func, x)
    
    print("\nCount\tx0\t\tepsilon")
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
        if math.isnan(xnew):
            print("NaN encountered. Newton-Raphson method failed to converge.")
            return None 
        
        epsilon = abs(xnew - x0)
        if epsilon < tolerance: 
            break
        
        x0 = xnew
        print(f"{i}\t{x0:.6f}\t{epsilon:.6f}")
    return xnew, i

def secMethod(func, x0, x00, tolerance, maxIter, batasDivergen):
    x = sym.symbols('x')
    
    print("Count\tx00\t\tx0\t\tf(x00)\t\tf(x0)\t\txnew\t\tepsilon")
    for i in range(maxIter):
        func_value = func.subs(x, x0)
        func_value_old = func.subs(x, x00)
        
        if abs(x0) > batasDivergen:
            print("Divergent")
            return None
        
        xnew = x0 - func_value * (x00 - x0) / (func_value_old - func_value)
        epsilon = abs(xnew - x0)
        if epsilon < tolerance:
            break
        x00 = x0
        x0 = xnew
        print(f"{i}\t{x00:.6f}\t{x0:.6f}\t{func_value_old:.6f}\t{func_value:.6f}\t{xnew:.6f}\t{epsilon:.6f}")
    return xnew, i

def get_user_input(prompt, default_value):
    user_input = input(prompt)
    if user_input == "":
        return default_value
    return user_input

if __name__ == "__main__":
    x = sym.symbols('x')
    
    y_expression = input("Enter the function y(x): ")
    y = parse_expr(y_expression, transformations=transformations)
    
    tolerance = float(get_user_input("Enter tolerance (default: 1e-6): ", 1e-6))
    maxIter = int(get_user_input("Enter maximum iteration (default: 1000): ", 1000))
    batasDivergen = float(get_user_input("Enter divergence boundary (default: 1e6): ", 1e6))

    print("Choose a method:")
    print("1. Newton Raphson")
    print("2. Secant Method")
    print("3. Both")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice in [1, 3]:
        x0_NR = float(input("Enter initial guess x0 for Newton Raphson: "))
        x_root_NR, iterations_NR = nRaphson(y, x0_NR, tolerance, maxIter, batasDivergen)
        print("Using Newton Raphson, the value of the root is %.6f at %d iterations" % (x_root_NR, iterations_NR))
    if choice in [2, 3]:
        x0_SEC = float(input("Enter initial guess x0 for Secant Method: "))
        x00_SEC = float(input("Enter another initial guess x00 for Secant Method: "))
        x_root_SEC, iterations_SEC = secMethod(y, x0_SEC, x00_SEC, tolerance, maxIter, batasDivergen)
        print("Using Secant Method, the value of the root is %.6f at %d iterations" % (x_root_SEC, iterations_SEC))

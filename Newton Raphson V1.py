def nRaphson(func, derivfunc, x, tolerance = 0.0001, maxIter = 1000):
    for i in range(maxIter):
        xnew = x - func(x)/derivfunc(x)
        if abs(xnew - x) < tolerance: break
        x = xnew
    return xnew, i

y = lambda x: x*x*x - 4*x*x + 1
dy = lambda x: 3*x*x - 8*x

x, n = nRaphson(y, dy, 0.5)
print ("The value of the root is %.4f at %d interations" % (x, n))


# Newton Raphson Algorithm
# 1. Find f'(x) and define Newton Raphson equation
# 2. Guess an initial value of x for the first iteration
# 3. Substitute x in the Newton Raphson equation and calculate xnew
# 4. if | xnew - x | < tolerance, stop iterations and output xnew
# 5. If the number of iterations reaches an assumed maximum, stop 
# 6. Else set x = xnew and go to step 3 until a condition in 4 or 5 is met
from sympy import *

x = symbols('x')
f = (1 + (1 / x)) ** x
result = limit(f, x, oo)
print (result)
print (result.evalf())
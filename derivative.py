from sympy import *

x = symbols('x')
f = x**2
# Вычисляем производную
dx_f = diff(f)
print(dx_f)
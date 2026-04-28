from sympy import *

# Объявляем символ x для SymPy
x = symbols('x')

# Объявляем функцию через обычный синтаксис Python
f = x**2 + 1

# Вычисляем интеграл от функции по x в интервале от x = 0 до x = 1
area = integrate(f, (x, 0, 2))

print(area)
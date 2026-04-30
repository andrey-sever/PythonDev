from sympy import *

# Объявляем переменные для SymPy
x, i, n = symbols('x i n')

# Объявляем функцию и интервал
f = x**2 + 1
lower, upper = 0, 1

# Вычисляем ширину и высоту каждого прямоугольника с индексом i
delta_x = ((upper - lower) / n)
x_i = (lower + delta_x * i)
fx_i = f.subs(x, x_i)

# Перебираем все n прямоугольников и суммируем их площади
n_rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit()

# Вычисляем площадь,
# устремив число прямоугольников n к бесконечности
area = limit(n_rectangles, n, oo)
print(area)
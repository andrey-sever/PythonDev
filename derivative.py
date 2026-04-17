from sympy import *

x = symbols('x')
f = x**2
# Вычисляем производную
dx_f = diff(f)
print("dx_f: ", dx_f)

# y = x2 + 1
# z = y3 - 2
# z = (x2 + 1)3 - 2
z = (x**2 + 1)**3 - 2
dz_dx = diff(z, x)
print("dz_dx: ", dz_dx)

x, y = symbols('x y')
# Производная первой функции
# Задаем имя с нижним подчеркиванием, чтобы не было конфликта переменных
_y = x**2 + 1
dy_dx = diff(_y)
# Производная второй функции
z = y**3 - 2
dz_dy = diff(z)
# Вычисляем производную с помощью цепного правила
# и без него, подставляем функцию y
dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
dz_dx_no_chain = diff(z.subs(y, _y))
# Цепное правило работает:
# оба варианта дают одинаковый результат
print(dz_dx_chain)
print(dz_dx_no_chain)

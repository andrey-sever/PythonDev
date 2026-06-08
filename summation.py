from sympy import *

summation = sum(2*i for i in range(1, 6))
print(summation)

x = [2, 10, 25]
n = len(x)
summation2 = sum(10*x[i] for i in range(0, n))
print(summation2)

i,n = symbols('i n')
# перебирает элементы i от 1 до n,
# затем умножает и суммирует
summation = Sum(2*i,(i,1,n))
# задает n равным 5,
# перебирает числа от 1 до 5
up_to_5 = summation.subs(n, 5)
print(up_to_5.doit())
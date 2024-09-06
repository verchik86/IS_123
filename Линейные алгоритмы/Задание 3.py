from math import sqrt
x = int(input('Введите число = '))
a = x % 10
one = x // 10
two = one % 10
three = one // 10
print(three, two, a, sep=' ')
S = int(three+two+a)
print('Сумма ',S)
print('Квадратный корень = ', sqrt(S))
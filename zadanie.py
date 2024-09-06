print('Задача 1')
b1 = int(input('Первое основание'))
b2 = int(input('Второе основание'))
h = int(input('Высота трапеции'))
S = (b1 + b2) / 2 * h
print (S)
print ('Задача 2')
a = str(input('Первое слово'))
b = str(input('Второе слово'))
c = str(input('Третье слово'))
print (a, b, c)
print('Задача 3')
x = int(input('Введите число'))
a1 = x // 100
a2 = x % 100 // 10
a3 = x % 10
sum = a1 + a2 + a3
cor = sum ** 0.5
print("Сумма чисел =", sum, "Корень суммы чисел равен", cor)
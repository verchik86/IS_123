print('Задание 1')
b1 = int(input('Число 1'))
b2 = int(input('Число 2'))
zn = b1 > b2
if zn == True:
    print(b1, "больше", b2)
else:
    print(b2, "больше", b1)
print('задание 2')
x = int(input('Число X'))
if x >= 0:
    y = 2 * x - 1
else:
    y = x ** 2
print(y)
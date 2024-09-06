# print('Задание 1')
# x = int(input('Число км'))
# y = int(input('Необходимые км'))
# den = 0
# while x <= y:
#     x = x * 1.1
#     den += 1
# print ('бег занял', den)
print ('Задание 2')
x = int(input('Стартовый вклад'))
p = int(input('Проценты'))
y = int(input('Ожидаемая сумма вклада'))
p = p / 100
god = 0
while y > x:
    x = x * (1 + p)
    god += 1
print('Для достижения суммы', y, 'понадобилось', god, 'лет')
x = int(input("Трехзначное число: "))
a = int(x // 100)
b = int((x//10)%10)
c = int(x % 10)
suma = a + b + c
print("S = ", suma)
k = suma**0.5
num = round(k, 2)
print("K = ", num)
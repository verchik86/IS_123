x = int(input())
a = x % 10
b = x // 10 % 10
c = x // 100
S = a + b + c
K = S ** 0.5
print(S, K)
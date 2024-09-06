x = int(input())
p = int(input())
y = int(input())
o = x
u = 0
while o <= y:
    o = p * 0.01 * o + o
    u = u + 1
else:
    print(u)
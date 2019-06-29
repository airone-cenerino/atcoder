import math


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
# 最大公約数


a, b, c, d = map(int, input().split())  # 複数数値入力

# cとdの最小公倍数
lcm = c * d / gcd(c, d)

# print(lcm)
# print(b - a + 1)
# print(int(b / c) - int((a - 1) / c))
# print(int(b / d) - int((a - 1) / d))
# print(int(b/lcm)-int((a-1)/lcm))
# print(b - a + 1 - math.floor(b / c) - math.floor(b/d) +
# math.floor((a-1) / c) + math.floor((a-1)/d) + (math.floor(b/lcm) - math.floor((a-1)/lcm)))
print(int(b - a + 1 - b // c - b//d +
          (a-1) // c + (a-1)//d + ((b//lcm) - (a-1)//lcm)))

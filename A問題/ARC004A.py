import math

n = int(input())
x = [0]*n
y = [0] * n
ans = 0

for i in range(n):
    x[i], y[i] = map(int, input().split())  # 複数数値入力

for i in range(n - 1):
    for j in range(i+1, n):
        if ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) > ans:
            ans = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2

print(math.sqrt(ans))

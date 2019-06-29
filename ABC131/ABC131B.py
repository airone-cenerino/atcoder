n, l = map(int, input().split())  # 複数数値入力
minaji = float('inf')
ans = 0
for i in range(n):
    if abs(minaji) > abs(i + l):
        minaji = i + l
    ans += i+l

print(ans - minaji)

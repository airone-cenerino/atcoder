a, b = map(int, input().split())  # 複数数値入力

ans = 0
while a <= b:
    a *= 2
    ans += 1

print(ans)

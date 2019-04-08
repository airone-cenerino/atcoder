a, b, c = map(int, input().split())  # 複数数値入力

d = min(a, b)
for i in reversed(range(d)):
    if a % (i + 1) == 0 and b % (i + 1) == 0:
        c -= 1

    if c == 0:
        print(i + 1)
        break

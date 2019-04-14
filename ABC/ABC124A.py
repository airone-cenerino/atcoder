a, b = map(int, input().split())  # 複数数値入力

if a == b:
    print(a * 2)
else:
    print(max(a, b)*2-1)

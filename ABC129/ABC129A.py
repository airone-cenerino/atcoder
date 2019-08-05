a, b, c = map(int, input().split())  # 複数数値入力
print(min(a+b, b+c, c+a))
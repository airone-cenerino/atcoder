r, D, x = map(int, input().split())  # 複数数値入力

for i in range(10):
    x = x*r -D
    print(x)
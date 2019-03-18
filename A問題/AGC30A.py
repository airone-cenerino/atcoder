a, b, c = map(int, input().split())  # 複数数値入力

if a + b >= c-1:
    print(b + c)
else:
    print(a+b+1+b)

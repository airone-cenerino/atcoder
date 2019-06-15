N = int(input())  # 数値入力
c = list(map(int, input().split()))  # 複数数値入力(リスト格納)
ans = float("inf")  # 無限

for i in range(1, N):
    a = sum(c[0:i])
    b = sum(c[i:N])

    if ans > abs(a - b):
        ans = abs(a-b)

print(ans)

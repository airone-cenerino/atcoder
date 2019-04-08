N = int(input())  # 数値入力
X = [0] * N
U = [0] * N

for i in range(N):
    X[i], U[i] = input().split()
    X[i] = float(X[i])

ans = 0
for i in range(N):
    if U[i] == "JPY":
        ans += X[i]
    else:
        ans += X[i] * 380000

print(ans)

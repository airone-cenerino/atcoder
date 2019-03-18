N, M, C = map(int, input().split())  # 複数数値入力
B = list(map(int, input().split()))

A = [0]*N
for i in range(N):
    A[i] = list(map(int, input().split()))

ans = 0
for i in range(N):
    if sum([x * y for (x, y) in zip(A[i], B)]) + C > 0:
        ans += 1

print(ans)

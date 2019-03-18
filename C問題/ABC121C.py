import numpy as np

N, M = map(int, input().split())  # 複数数値入力

A = [[0, 0]] * N
for i in range(N):
    A[i] = list(map(int, input().split()))  # 複数数値入力

A = np.array(A, dtype=np.float64)
A = A[np.argsort(A[:, 0])]

ans = 0
for i in range(N):
    if M >= A[i][1]:
        M -= A[i][1]
        ans += A[i][0] * A[i][1]
    else:
        ans += A[i][0] * M
        break

print(int(ans))

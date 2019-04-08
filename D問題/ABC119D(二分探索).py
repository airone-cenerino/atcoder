import bisect

A, B, Q = map(int, input().split())  # 複数数値入力
S = [0] * A
T = [0] * B
X = [0] * Q
for i in range(A):
    S[i] = int(input())
for i in range(B):
    T[i] = int(input())
for i in range(Q):
    X[i] = int(input())

S.insert(0, -float("inf"))
S.append(float("inf"))
T.insert(0, -float("inf"))
T.append(float("inf"))

for i in range(Q):
    b = bisect.bisect_right(S, X[i])
    d = bisect.bisect_right(T, X[i])
    res = float("inf")
    for s in [S[b - 1], S[b]]:
        for t in [T[d - 1], T[d]]:
            d1 = abs(s - X[i]) + abs(t - s)  # 先に神社
            d2 = abs(t - X[i]) + abs(t - s)  # 先に寺
            res = min(res, d1, d2)

    print(res)

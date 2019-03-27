import numpy as np

N, Q = map(int, input().split())  # 複数数値入力
S = list(input())  # 一文字ずつ格納
L = []
R = []

for i in range(Q):
    l, r = map(int, input().split())  # 複数数値入力
    L.append(l)
    R.append(r)

list = []
flg = 0
for s in S:
    if s == "A" and flg == 0:
        flg = 1
    elif s == "C" and flg == 1:
        list.append(1)
        list.append(2)
        flg = 0
    elif flg == 1:
        list.append(0)
        list.append(0)
    else:
        list.append(0)

for i in range(Q):
    S = list[L[i] - 1:]
    S = S[:R[i] - L[i] + 1]
    if S[0] == 2:
        S = S[1:]
    if S[-1] == 1:
        S = S[:-2]

    S = np.array(S)
    print(int(np.sum(S)/3))

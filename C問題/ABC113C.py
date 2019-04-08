N, M = map(int, input().split())  # 複数数値入力
L = [[] for i in range(N)]
P = list()
Y = list()

for i in range(M):
    p, y = map(int, input().split())  # 複数数値入力
    P.append(p)
    Y.append(y)
    L[p - 1].append(y)

for i in range(N):
    L[i].sort()

for i in range(M):
    print('{:06}'.format(P[i]), end="")
    print('{:06}'.format(L[P[i]-1].index(Y[i])+1))

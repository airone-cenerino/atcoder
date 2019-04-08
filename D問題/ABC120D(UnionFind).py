class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * (n+1)  # parentは親の番号を格納。　親だった時は-サイズを格納。

    # 親の番号を返す
    def root(self, A):
        if self.parent[A] < 0:
            return A
        else:
            return self.root(self.parent[A])

    # サイズを返す
    def size(self, A):
        return - self.parent[self.root(A)]

    # AとBをくっつける(直接ではなくroot(A)とroot(B)を繋げる)
    def connect(self, A, B):
        A = self.root(A)
        B = self.root(B)

        if A == B:  # 既に同じ塊内にいる
            return False

        if self.size(A) < self.size(B):
            A, B = B, A

        self.parent[A] += self.parent[B]  # サイズを更新
        self.parent[B] = A

        return True


N, M = map(int, input().split())  # 複数数値入力
A = list()
B = list()
for i in range(M):
    a, b = map(int, input().split())  # 複数数値入力
    A.append(a)
    B.append(b)

ans = [N * (N - 1) / 2] * M  # とりあえず不便性最大で初期化
Uni = UnionFind(N)

for i in reversed(range(1, M)):
    if Uni.root(A[i]) != Uni.root(B[i]):    # 島同士が繋がってなかったとき
        ans[i - 1] = ans[i] - Uni.size(A[i]) * Uni.size(B[i])
        Uni.connect(A[i], B[i])
    else:
        ans[i-1] = ans[i]

for i in range(len(ans)):
    print(int(ans[i]))

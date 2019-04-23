class UnionFind:
    def __init__(self, n):
        # parentは親の番号を�?�納。　親�?った時は-サイズを�?�納�?
        self.parent = [-1] * (n+1)

    # 親の番号を返す
    def root(self, A):
        if self.parent[A] < 0:
            return A
        else:
            return self.root(self.parent[A])

    # サイズを返す
    def size(self, A):
        return - self.parent[self.root(A)]

    # AとBをくっつける(直接ではなくroot(A)とroot(B)を繋げ�?)
    def connect(self, A, B):
        A = self.root(A)
        B = self.root(B)

        if A == B:  # 既に同じ塊�??に�?�?
            return False

        if self.size(A) < self.size(B):
            A, B = B, A

        self.parent[A] += self.parent[B]  # サイズを更新
        self.parent[B] = A

        return True


N, M = map(int, input().split())  # �?数数値入�?
A = list()
B = list()
for i in range(M):
    a, b = map(int, input().split())  # �?数数値入�?
    A.append(a)
    B.append(b)

ans = [N * (N - 1) / 2] * M  # とりあえず不便性最大で初期�?
Uni = UnionFind(N)

for i in reversed(range(1, M)):
    if Uni.root(A[i]) != Uni.root(B[i]):    # 島同士が繋がってなかったと�?
        ans[i - 1] = ans[i] - Uni.size(A[i]) * Uni.size(B[i])
        Uni.connect(A[i], B[i])
    else:
        ans[i-1] = ans[i]

for i in range(len(ans)):
    print(int(ans[i]))

N, A, B, C = map(int, input().split())  # 複数数値入力
L = [0] * N
for i in range(N):
    L[i] = int(input())


def dfs(depth, a, b, c):    # 深さは何本目の竹まで場合分けしたかを示す  a,b,cにはA,B,Cに割り当てられている竹の長さの和が入っている　戻り値はMP
    if depth == N:
        # ABCのどれかが1本も割り当てられていない場合はだめなのでINFを返す
        return abs(a-A)+abs(b-B)+abs(c-C) - 30 if min(a, b, c) > 0 else 1000000000

    ret0 = dfs(depth + 1, a, b, c)  # depth本目の竹を使わない
    # depth本目の竹をAを作るのに使用する    コストを足して、長さには使用する竹の長さを足してやる
    ret1 = dfs(depth + 1, a + L[depth], b, c) + 10
    ret2 = dfs(depth + 1, a, b + L[depth], c) + 10  # depth本目の竹をBを作るのに使用する
    ret3 = dfs(depth + 1, a, b, c + L[depth]) + 10  # depth本目の竹をCを作るのに使用する

    return min(ret0, ret1, ret2, ret3)  # 一番小さいMPを返す


print(dfs(0, 0, 0, 0))

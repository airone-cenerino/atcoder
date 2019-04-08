N, M = map(int, input().split())  # 複数数値入力
X = list(map(int, input().split()))  # リスト入力（数値）  map関数はリストの各要素に対して関数を適用してくれ
X.sort()

if N >= M:
    print(0)
else:
    list = list()
    last = 0
    flg = True
    for x in X:
        if flg == True:
            last = x
            flg = False
            continue

        list.append(x - last)
        last = x

    list.sort()

    for i in range(N-1):
        list.pop(-1)
    print(sum(list))

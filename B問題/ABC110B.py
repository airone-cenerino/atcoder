N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))  # リスト入力（数値）  map関数はリストの各要素に対して関数を適用してくれる
y = list(map(int, input().split()))  # リスト入力（数値）  map関数はリストの各要素に対して関数を適用してくれる

minX = max(x) + 1
maxY = min(y)

if X < minX and maxY <= Y and minX <= maxY:
    print("No War")
else:
    print("War")

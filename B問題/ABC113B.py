N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))  # リスト入力（数値）  map関数はリストの各要素に対して関数を適用してくれる

l = list()
for h in range(len(H)):
    l.append(abs(T - H[h] * 0.006 - A))

print(l.index(min(l))+1)

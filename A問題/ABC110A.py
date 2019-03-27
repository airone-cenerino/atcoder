l = list(map(int, input().split()))  # リスト入力（数値）  map関数はリストの各要素に対して関数を適用してくれる

ans = l.pop(l.index(max(l)))*10
ans += sum(l)

print(ans)

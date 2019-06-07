N = int(input())  # 数値入力
H = list(map(int, input().split()))  # リスト入力（数値）  map関数はリストの各要素に対して関数を適用してくれる

# test

ans = 0
while sum(H) != 0:
    i = 0
    while(i < N):
        if(H[i] == 0):
            i += 1
        else:
            ans += 1
            while((i < N) and (H[i] > 0)):
                H[i] -= 1
                i += 1

print(ans)

n, m = map(int, input().split())  # 複数数値入力
s = list()

for i in range(m):
    tmp = list(map(int, input().split()))  # 複数数値入力(リスト格納)
    s.append(tmp[1:])

p = list(map(int, input().split()))  # 複数数値入力(リスト格納)

# print(s)
ans = 0
# bit全探索
for i in range(2 ** n):
    flg = 0
    onswitchkosuu = [0] * m
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # j番目のスイッチがついているならここに入るよ
            for k in range(m):  # この中で各電球についてj番目のスイッチと接続されているかを確認
                if j+1 in s[k]:
                    onswitchkosuu[k] += 1

   # print(onswitchkosuu)    # これには各電球について何個のスイッチが押されているかが書いてある
    # この下で各電球がつくのかどうかを検証

    for j in range(m):
        if onswitchkosuu[j] % 2 != p[j]:
            flg = 1

    if flg == 0:
        ans += 1

print(ans)

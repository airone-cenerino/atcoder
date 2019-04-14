n, k = map(int, input().split())  # 複数数値入力
s = list(input())  # 一文字ずつ格納
list = list()
last = s[0]
ren = 0
for i in range(len(s)):
    if last == s[i]:
        ren += 1
    else:
        list.append(ren)
        ren = 1

    last = s[i]
list.append(ren)


print(list)

ans = 0
nagasa = len(list)
#　1始まり1終わり:
if s[0] == "1" and s[-1] == "1":
    for i in range(nagasa - 2 * k):
        i = sum(list[i: i + 2 * k + 1])

        if ans < i:
            ans = i

# 0始まり0終わり
if s[0] == "0" and s[-1] == "0":
    for i in range(nagasa - 1):
        if i == 0 or i == nagasa - 2:
            i = sum(list[i: i + 2 * k])
        else:
            i = sum(list[i: i + 2 * k + 1])

        if ans < i:
            ans = i

        print(i)


print(ans)

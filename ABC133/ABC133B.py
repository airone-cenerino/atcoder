import math

n, d = map(int, input().split())  # 複数数値入力
li = list()
for i in range(n):
    li.append(list(map(int, input().split())))  # 複数数値入力(リスト格納)
ans = 0

for i in range(n):
    for j in range(i + 1, n):
        sum = 0
        for k in range(d):
            sum += (li[i][k] - li[j][k]) ** 2

        if float.is_integer(math.sqrt(sum)):
            ans += 1

print(ans)

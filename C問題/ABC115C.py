N, K = map(int, input().split())  # 複数数値入力
li = list()
for n in range(N):
    li.append(int(input()))

li.sort()

ans = float("inf")
for i in range(N - K + 1):
    if ans > li[i + K - 1] - li[i]:
        ans = li[i + K - 1] - li[i]
print(ans)

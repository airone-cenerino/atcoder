n, k = map(int, input().split())  # 複数数値入力
a = list(map(int, input().split()))  # 複数数値入力(リスト格納)
li = list()
sum = 0
for num in a:
    sum += num
    li.append(sum)

ans = 0
last=0
for i in range(len(li)):
    if li[i] < k:
        continue
    ans +=last+1
    
    while li[i] - li[last] >= k:
        last += 1
        ans += 1

print(ans)
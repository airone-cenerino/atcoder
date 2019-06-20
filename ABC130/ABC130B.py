n, x = map(int, input().split())  # 複数数値入力
l = list(map(int, input().split()))  # 複数数値入力(リスト格納)
ans =1
sum =0
for num in l:
    sum += num
    if sum>x:
        break
    else:
        ans+=1

print(ans)
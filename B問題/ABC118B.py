n,m=map(int, input().split())  #複数数値入力
list1 = [0] * n

for i in range(n):
    list1[i]=list(map(int, input().split()))  #リスト入力（数値）
    list1[i].pop(0)

ans = 0

for i in range(m):
    check = 0
    for j in range(n):
        if not i+1 in list1[j]:
            check =1
            break
    
    if check == 0:
        ans += 1


print(ans)
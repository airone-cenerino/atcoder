n = int(input())  # 数値
v = input().split()  # 空白区切りでリストへ
c = input().split()  # 空白区切りでリストへ

ans = 0
for i in range(n):
    if int(v[i]) > int(c[i]):
        ans += int(v[i]) - int(c[i])
print(ans)

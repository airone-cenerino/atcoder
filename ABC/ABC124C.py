str = list(input())  # 一文字ずつ格納
last = str[0]
ans = 0

for i in range(1, len(str)):
    if last == str[i]:
        ans += 1
        if last == "0":
            last = '1'
        else:
            last = '0'
    else:
        last = str[i]


print(ans)

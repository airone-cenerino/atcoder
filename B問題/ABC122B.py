S = list(input())  # 一文字ずつ格納
ans = 0
tmp = 0
for s in S:
    if s != "A" and s != "T" and s != "G" and s != "C":
        ans = max(ans, tmp)
        tmp = 0
    else:
        tmp += 1

ans = max(ans, tmp)

print(ans)

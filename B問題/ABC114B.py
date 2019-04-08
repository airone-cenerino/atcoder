str = list(input())  # 一文字ずつ格納
ans = 1000

for i in range(len(str) - 2):
    sa = abs(int(str[i]) * 100 + int(str[i+1]) * 10 + int(str[i + 2]) - 753)
    ans = min(ans, sa)

print(ans)

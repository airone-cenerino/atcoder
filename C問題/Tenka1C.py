n = int(input())  # 数値入�?
str = list(input())  # 一�?字ずつ格�?
dotto = str.count(".")
ans = dotto
syapu = 0

for i in range(0, n):
    if str[i] == ".":
        dotto -= 1
    else:
        syapu += 1

    if dotto + syapu < ans:
        ans = dotto + syapu

print(ans)

n = int(input())  # 数値入力
str = list(input())  # 一文字ずつ格納
newstr = []
new1str = []

for i in range(n):
    if str[i] == "#":
        new1str = str[i:]
        break

n1 = len(new1str)
for i in range(n1):
    if new1str[n1-1-i] == ".":
        newstr = new1str[:n1-i]
        break

if len(newstr) == 0:
    print(0)
else:
    print(min(newstr.count("."), newstr.count("#")))

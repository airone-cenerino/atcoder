n = int(input())
last = ""
flg = 0
li = []
for i in range(n):
    s = input()
    str = list(s)  # 一文字ずつ格納
    if last == "":
        last = str[-1]
        li.append(s)
        continue

    if str[0] != last or s in li:
        flg = 1

    last = str[-1]
    li.append(s)


if flg == 0:
    print("Yes")
else:
    print("No")

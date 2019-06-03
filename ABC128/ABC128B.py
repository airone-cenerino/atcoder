n = int(input())  # 数値入力
li = list()

for i in range(n):
    s, p = input().split()
    li.append([s, int(p), i+1])

li.sort()
lastcity = li[0][0]
newli = list()

for i in range(n):
    if lastcity == li[i][0]:
        newli.append([li[i][1], li[i][2]])
        lastcity = li[i][0]
    else:
        newli = newli[::-1]
        for tmp in newli:
            print(tmp[1])
        newli = list()
        newli.append([li[i][1], li[i][2]])
        lastcity = li[i][0]

newli = newli[::-1]
for tmp in newli:
    print(tmp[1])

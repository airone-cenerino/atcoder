n,m=map(int, input().split())  #複数数値入力
a=list(map(int, input().split()))  #リスト入力（数値)
needNum = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

a.sort()
need = list()
for i in range(m):
    need.append(needNum[a[i]])

minNum = a[need.index(min(need))]  #必要マッチ棒が一番少ない数
minNeed = min(need) #必要マッチ棒が一番少ない数の必要数

digit = n//minNeed
remain = n % minNeed


out = 0
for i in range(digit):
    if i == digit-1:
        if remain != 0:
            for j in range(m):
                if minNeed +remain == needNum[a[-1-j]]:
                    out = a[-1-j]
                    break
        else:
            out = minNum
    elif remain != 0:
        for j in range(m):
            if minNeed+remain >= needNum[a[-1-j]]:
                out = a[-1-j]
                remain -= needNum[a[-1-j]]-minNeed
                break
    else:
        out = minNum

    print( out, end="")
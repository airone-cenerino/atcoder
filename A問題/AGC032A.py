N = int(input())  # 数値入力
b = list(map(int, input().split()))  # リスト入力（数値）  map関数はリストの各要素に対して関数を適用してくれる

b.reverse()
ans = []

while b:
    check = 0
    tmp = 0
    for i in b:
        if i == len(b) - tmp:
            ans.append(b.pop(tmp))
            check = 1
            break

        tmp += 1

    if check == 0:
        check = 2
        break


if check == 2:
    print(-1)
else:
    ans.reverse()
    for i in ans:
        print(i)

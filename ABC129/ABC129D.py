H, W = map(int, input().split())  # 複数数値入力

li = list()
for i in range(H):
    li.append(list(input()))  # 1文字区切りでリスト格納

ans = 0
for h in range(H):
    for w in range(W):
        akarukunarutoko = 1
        # print("------")
        if li[h][w] == "#":
            continue

        n = 1
        while True:
            if h + n >= H:
                break
            if li[h + n][w] == "#":
                break
            n += 1
        akarukunarutoko += n-1

        n = 1
        while True:
            if h - n < 0:
                break
            if li[h - n][w] == "#":
                break
            n += 1
        akarukunarutoko += n-1
        # print(akarukunarutoko)

        n = 1
        while True:
            if w + n >= W:
                break
            if li[h][w+n] == "#":
                break
            n += 1
        akarukunarutoko += n-1
        # print(akarukunarutoko)

        n = 1
        while True:
            if w - n < 0:
                break
            if li[h][w-n] == "#":
                break
            n += 1
        akarukunarutoko += n-1
        # print(akarukunarutoko)
        if ans < akarukunarutoko:
            ans = akarukunarutoko

print(ans)

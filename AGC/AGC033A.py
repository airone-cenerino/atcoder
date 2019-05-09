import queue

h, w = map(int, input().split())  # 複数数値入力
li = []
x = [1, -1, 0, 0]
y = [0, 0, 1, -1]
q = queue.Queue()
ans = 0

for i in range(h):
    strr = list(input())

    for j in range(w):
        if strr[j] == "#":
            q.put(str(i) + "," + str(j))

    li.append(strr)

while not q.empty():
    qSize = q.qsize()
    height = [0] * qSize
    width = [0] * qSize
    for j in range(qSize):
        height[j], width[j] = map(int, q.get().split(","))

# もうすでに囲まれているなら見る必要はない
    for j in range(qSize):
        for i in range(4):
            try:
                if li[height[j] + y[i]][width[j] + x[i]] == ".":
                    if (width[j] == 0 and width[j] + x[i] == -1) or (width[j] == w-1 and width[j] + x[i] == w) or (height[j] == h-1 and height[j] + y[i] == h) or (height[j] == 0 and height[j] + y[i] == -1):
                        break
                    li[height[j] + y[i]][width[j] + x[i]] = "#"


                    q.put(str(height[j] + y[i]) + "," + str(width[j] + x[i]))
            except:
                pass

    ans += 1

print(ans - 1)

li = []

for i in range(5):
    a = int(input())
    li.append(a)

b = int(input())

last = 0
flg = 0
for i in li:
    for j in li:
        if abs(i - j) > b:
            flg = 1

        last = i

if flg == 0:
    print("Yay!")
else:
    print(":(")

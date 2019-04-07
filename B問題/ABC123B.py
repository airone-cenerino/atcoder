amari = 10

li = []
for i in range(5):
    a = int(input())
    if a % 10 == 0:
        li.append(a)
    else:
        li.append((a // 10 + 1) * 10)
        if a % 10 < amari:
            amari = a % 10


print(sum(li)-10+amari)

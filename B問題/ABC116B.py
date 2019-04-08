a = int(input())

l = [a]
b = a
c = 1

while True:
    if b % 2 == 0:
        b = int(b/2)
    else:
        b = 3 * b + 1

    c += 1

    if b in l:
        break

    l.append(b)

print(c)

n = int(input())

l0 = 2
l1 = 1

for i in range(n):
    tmp = l1
    l1 = l1 + l0
    l0 = tmp

print(l0)

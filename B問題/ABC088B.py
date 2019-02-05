n = int(input())
l = input().split()
for i in range(n):
    l[i] = int(l[i])
l.sort()
l.reverse()

a=0
b=0

for i in range(n):
    if i%2==0:
        a+=l.pop(0)
    else:
        b+=l.pop(0)

print(a-b)
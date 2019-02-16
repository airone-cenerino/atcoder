n = int(input())
l=input().split()
for i in range(n):
    l[i] = int(l[i])

l.sort()
max = l.pop(-1)
sum = sum(l)
if sum>max:
    print("Yes")
else:
    print("No")
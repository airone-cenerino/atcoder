a = int(input())  # 数値入力

l = list()
for i in range(a):
    l.append(int(input()))

l.sort()
ans = int(l.pop(len(l) - 1)/2)
ans += sum(l)

print(ans)

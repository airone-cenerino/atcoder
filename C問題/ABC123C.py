N = int(input())
li = []

for i in range(5):
    a = int(input())
    li.append(a)

ans = 0
if N % min(li) == 0:
    ans += N // min(li)
else:
    ans += N // min(li) + 1

print(ans+4)

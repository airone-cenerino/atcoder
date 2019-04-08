a, b = map(int, input().split())  # 複数数値入力
c = list()
t = list()
ans = float("inf")

for i in range(a):
    C, T = map(int, input().split())
    if T > b:
        continue

    ans = min(ans, C)

if ans == float("inf"):
    print("TLE")
else:
    print(ans)

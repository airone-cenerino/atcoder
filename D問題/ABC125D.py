n = int(input())
a = list(map(int, input().split()))  # 複数数値をリストに格納
ans = 0

a.sort()
num = 0
#  マイナスの個数が偶数なら全部正にして和をとる
# 基数なら全部せいにして絶対値小さいやつを引く

for i in range(n):
    if a[i] < 0:
        num += 1

# numはマイナスの数
a = list(map(abs, a))
if num % 2 == 0:
    print(sum(a))
else:
    a.sort()
    print(sum(a) - a[0]*2)

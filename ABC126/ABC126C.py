import math
n, k = map(int, input().split())  # 複数数値入力
ans = 0
num = int(math.log2(k)+1)    # 目が1の時に連続して表にならなくてはいけない数

for i in range(1, n+1):
    if i>=k:
        ans += 1
    else:
    #  print(max(math.ceil(math.log2(k/i)), 1))
        ans += 1/(2 ** max(math.ceil(math.log2(k/i)), 1) )

print(ans/n)
import numpy as np

N, Q = map(int, input().split())  # 複数数値入力
S = list(input())  # 一文字ずつ格納

dp = [0] * N
i = 0
flg = False
for str in S:
    if str == "C" and flg == True:
        dp[i] = dp[i - 1] + 1
        flg = False
    elif str == "A":
        flg = True
        dp[i] = dp[i-1]
    else:
        flg = False
        dp[i] = dp[i-1]
    i += 1

for i in range(Q):
    l, r = map(int, input().split())  # 複数数値入力
    print(dp[r-1]-dp[l-1])

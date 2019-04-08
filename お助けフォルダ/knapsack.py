n, w = map(int, input().split())
value = [0] * n
weight = [0] * n
dp = [[0]*110]*10010

for i in range(n):
    value[i], weight[i] = map(int, input().split())

for i in range(n):  # i個のもの
    for j in range(w+1):    # jまでの重さ
        if j >= weight[i]:  # もしi番目の物が入れられるなら  
            dp[i+1][j] = max(dp[i][j-weight[i]] + value[i], dp[i][j])   # 入れるときと入れないときとで大きい方をとる
        else:
            dp[i+1][j] = dp[i][j]   # 入れられないならそのまま

print(dp[n][w])

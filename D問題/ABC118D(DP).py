<<<<<<< HEAD
n,m=map(int, input().split())  #複数数値入力
A=list(map(int, input().split()))  #リスト入力（数値)
=======
n, m = map(int, input().split())  # 複数数値入力
A = list(map(int, input().split()))  # リスト入力（数値)
>>>>>>> 9a542c0c5432627e78d2f4be2afc0aa71e398a2e
num = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]

A.sort(reverse=True)    # 大きい順に並べる

dp = [-1*float("inf")]*(n+1)    # その本数で作れる最大の桁数
# dp初期化 (0本では0桁, 各数字を1つ作る場合は1桁)
dp[0] = 0
for a in A:
    if num[a] <= n:
        dp[num[a]] = 1

<<<<<<< HEAD
for i in range(1,n+1):
=======
for i in range(1, n+1):
>>>>>>> 9a542c0c5432627e78d2f4be2afc0aa71e398a2e
    for a in A:
        if i - num[a] >= 0:
            dp[i] = max(dp[i], dp[i-num[a]] + 1)

ans = ""
for i in range(dp[n]):  # 1桁ずつ考える
<<<<<<< HEAD
    for a in A: # 使える数1つずつ大きい方から考える
=======
    for a in A:  # 使える数1つずつ大きい方から考える
>>>>>>> 9a542c0c5432627e78d2f4be2afc0aa71e398a2e
        if n-num[a] >= 0 and dp[n-num[a]] == dp[n]-1:
            ans += str(a)
            n -= num[a]
            break
<<<<<<< HEAD
 
=======

>>>>>>> 9a542c0c5432627e78d2f4be2afc0aa71e398a2e
print(ans)

a = int(input())  # 数値入力
str = input()
str = list(str)
str_unique = list(set(str))


ans = 1
for moji in str_unique:
    ans *= str.count(moji) + 1

print((ans-1) % 1000000007)

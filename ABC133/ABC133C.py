l, r = map(int, input().split())  # 複数数値入力

lm = l % 2019
rm = r % 2019

if (r - l) + lm < 2019:  # 間に2019の倍数はない
    print((lm*(lm+1)) % 2019)
else:
    print(0)

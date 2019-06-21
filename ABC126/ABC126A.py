a, b = map(int, input().split())  # 複数数値入力
str = list(input())

if str[b-1] <= 'z' and str[b-1] >='a':
    str[b-1] = str[b-1].upper()
else:
    str[b-1] = str[b-1].lower()

for s in str:
    print(s, end="")
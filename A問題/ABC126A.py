a, b = map(int, input().split())
str1 = list(input())  # 1文字区切りでリスト格納

if 'a' <= str1[b-1] and 'z'>=str1[b-1]:
    str1[b-1] = str1(str1[b-1]).upper()
    for s in str1:
        print(s, end="")
else:
    str1[b-1] = str(str1[b-1]).lower()
    for s in str1:
        print(s, end="")
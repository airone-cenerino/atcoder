a = int(input())  # 数値入力
str = list(input())  # 一文字ずつ格納
if str.count("R") > str.count("B"):
    print("Yes")
else:
    print("No")

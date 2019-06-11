a = int(input())  # 数値入力
b = a%100
a = int(a/100)

if a>0 and a<=12:
    if b>0 and b<=12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if b>0 and b<=12:
        print("YYMM")
    else:
        print("NA")
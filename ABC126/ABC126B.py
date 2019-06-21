a = int(input())  # 数値入力
b = int(a/100)
c = a%100
if b>0 and b<=12:
    if c>0 and c<=12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if c>0 and c<=12:
        print("YYMM")
    else:
        print("NA")
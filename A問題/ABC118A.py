a,b=map(int, input().split())  #複数数値入力

if b % a == 0:
    print(a+b)
else:
    print(b-a)
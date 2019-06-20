w, h, x, y = map(float, input().split())  # 複数数値入力

yoko = min((w-x)*h, x*h)
tate = min((h-y)*w, y*w)
naname = min()


if yoko == tate:
    print(str(yoko) + " 1")
else:
    print(str(max(yoko, tate))+ " 0")
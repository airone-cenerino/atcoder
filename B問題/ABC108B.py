a, b, c, d = map(int, input().split())  # 複数数値入力

print(str(c - (d - b)), " ", str(c - a + d), " ",
      str(a - (d - b)), " ", b+(c-a), sep=" ")

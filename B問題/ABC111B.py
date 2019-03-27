a = int(input())

for i in range(1, 10):
    if a <= i * 100 + i * 10 + i:
        print(i * 100 + i * 10 + i)
        break

import math

a, b = map(int, input().split())  # 複数数値入力

A = list()
B = list()

if b == 0:
    B = [0]
elif b == 1:
    B = [1]
else:
    for i in range(1, int(math.log2(b))+2):
        tmp = b // (2 ** i) * 2 ** (i - 1)

        if b % (2 ** i) < (2 ** (i-1)):
            plus = 0
        else:
            plus = b % (2 ** i) - 2 ** (i-1) + 1

        B.append(tmp + plus)

if a == 0:
    A = [0]
elif a == 1:
    A = [0]
else:
    for i in range(1, int(math.log2(a-1))+2):
        tmp = (a-1) // (2 ** i) * 2 ** (i - 1)

        if (a-1) % (2 ** i) < (2 ** (i-1)):
            plus = 0
        else:
            plus = (a-1) % (2 ** i) - 2 ** (i-1) + 1

        A.append(tmp + plus)

if b == 0:
    print(0)
else:
    ans = 0
    for i in range(0, int(math.log2(b)) + 1):
        if i >= len(A):
            ans += (B[i]) % 2 * 10 ** i
        else:
            ans += (B[i] - A[i]) % 2 * 10 ** i

    print(int(str(ans), 2))

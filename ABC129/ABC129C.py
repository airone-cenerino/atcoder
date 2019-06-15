def Fib(n):
    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(n-2):
            a, b = b, a + b
        return b


def main():
    N, M = map(int, input().split())  # 複数数値入力
    li = list()
    last = -1
    current = N
    ans = 1
    beforeBroken = 0
    for i in range(M):
        current = int(input())
        beforeBroken = current
        if last == current - 1 and last != 0:
            print(0)
            return

        if current != 1:
            li.append(current - last-2)
        last = current

    if M != 0:
        li.append(N - beforeBroken-1)
    else:
        li.append(N)
    for i in li:
        ans *= Fib(i+2)
    print(ans % 1000000007)


main()

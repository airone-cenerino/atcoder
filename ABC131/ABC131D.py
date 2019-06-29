def main():
    n = int(input())
    L = []

    for i in range(n):
        a, b = map(int, input().split())  # 複数数値入力
        L.append([b, a])

    L.sort()
    sum = 0
    for l in L:
        sum += l[1]
        if sum > l[0]:
            print("No")
            return

    print("Yes")

main()
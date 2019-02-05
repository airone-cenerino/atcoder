n = int(input())
lt=0
lx=0
ly = 0

for i in range(n):
    t, x, y = map(int, input().split())
    if abs(x-lx)+abs(y-ly) > t - lt or (abs(x-lx)+abs(y-ly)) % 2 != (t-lt) % 2:
        print("No")
        exit()

    lt=t
    lx=x
    ly=y

print("Yes")
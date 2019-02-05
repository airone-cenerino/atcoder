num = int(input())
l = input().split()
for i in range(num):
    l[i] = int(l[i])
ans = 0
tmp = 0

while True:
    for i in range(num):
        if(l[i]%2!=0):
            tmp=1
        
        l[i] /= 2
    if(tmp==1):
        break

    ans += 1


print(ans)

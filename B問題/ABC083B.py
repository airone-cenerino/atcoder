n,a,b = map(int, input().split())
ans =0

for i in range(1,n+1):
    num=i
    lst = []
    while i > 0:
        lst.append(i%10)
        i //= 10        # 切り捨て除算

    sum=0
    for j in lst:
        sum += j
    
    if sum>=a and sum<=b:
        ans+=num

print(ans)
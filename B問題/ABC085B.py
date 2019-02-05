n = int(input())
l = list()
for i in range(n):
    l.append(int(input()))

l.sort()
ans=1
for i in range(n-1):
    if(l[i]==l[i+1]):
        continue
    
    ans+=1

print(ans)
n = int(input())  # ���l
v = input().split()  # �󔒋�؂�Ń��X�g��
c = input().split()  # �󔒋�؂�Ń��X�g��

ans = 0
for i in range(n):
    if int(v[i]) > int(c[i]):
        ans += int(v[i]) - int(c[i])
print(ans)

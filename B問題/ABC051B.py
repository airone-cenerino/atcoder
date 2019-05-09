k, s = map(int, input().split())  # •¡””’l“ü—Í
ans = 0
for i in range(k + 1):
    for j in range(i, k + 1):
        for l in range(j, k + 1):
            if i + j + l == s:
                if i != j and j != l:
                    ans += 6
                elif i != j or j != l:
                    ans += 3
                else:
                    ans += 1

                break

print(ans)

str = input()
char_list = list(str)
ans = 0

for i in range(3):
    if char_list[i] == "1":
        ans = ans+1

print(ans)
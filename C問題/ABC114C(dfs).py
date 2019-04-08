N = int(input())  # 数値入力


def dfs(s):
    # 潜りすぎ防止
    if int(s) > N:
        return 0

    # 7,5,33がすべて含まれていたらret=1
    ret = 1 if all(s.count(c) > 0 for c in "753") else 0

    for c in "753":
        ret += dfs(s + c)  # 潜る

    return ret


print(dfs("0"))

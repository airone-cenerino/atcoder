a = int(input())  # 数値入力
a, b = map(int, input().split())  # 複数数値入力
c = list(map(int, input().split()))  # 複数数値入力(リスト格納)
l = input().split()  # 複数文字列入力（リスト格納）
str = list(input())  # 1文字区切りでリスト格納

print("hoge", end="")  # 改行なし

inf = float("inf")  # 無限

L = [[] for i in range(3)]  # 2重リストの初期化[[],[],[]]

print('{:06}'.format(333))  # フォーマット指定出力000333

list = list[::-1]   # リストを反対に

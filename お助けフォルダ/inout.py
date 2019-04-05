a = int(input())  # 数値入力
a, b = map(int, input().split())  # 複数数値入力
c = list(map(int, input().split()))  # リスト入力（数値）  map関数はリストの各要素に対して関数を適用してくれる
l = input().split()  # リスト入力
str = list(input())  # 一文字ずつ格納

print("hoge", end="")  # 改行なし出力

inf = float("inf")  # 無限

L = [[] for i in range(3)]  # 2次元リストの正しい初期化の方法 [[],[],[]]

print('{:06}'.format(333))  # 桁数指定出力 000333

list = list[::-1]   # リストを逆順に

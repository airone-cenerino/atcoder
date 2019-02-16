def main():
    n=int(input())  #数値入力
    a=list(map(int, input().split()))  #リスト入力（数値)
    num = a[0]

    for i in range(n-1):
        num = gcd(num, a[i+1])
    print(num)

# 最大公約数
def gcd(a, b):
  while b > 0:
    a, b = b, a%b
  return a

main()
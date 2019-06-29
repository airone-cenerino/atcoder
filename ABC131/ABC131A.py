def main():
    str = list(input())  # 1文字区切りでリスト格納
    last = ""
    for s in str:
        if s == last:
            print("Bad")
            return
        last = s

    print("Good")


main()

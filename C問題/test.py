splited = list(map(int, input().split("/")))


if int(splited[0]) < 2019:
    print("Heisei")
elif int(splited[1]) < 4:
    print("Heisei")
elif int(splited[2]) <= 30:
    print("Heisei")
else:
    print("TBD")

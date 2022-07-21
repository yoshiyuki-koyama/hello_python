# 関数の宣言
def Add(a:int, b:int):
    return a+b

def main():
    # print
    print("hello, world")

    # 標準入力
    name1 = input("Enter, your name.\n")
    print("1st: Your name is ", name1)
    name2 = input("Enter, your name AGAIN.\n")
    print("2nd: Your name is ", name1)

    # if文
    if name1 == name2:
        print("1st and 2nd name is SAME!")
    elif name1.lower() == name2.lower():
        print("1st and 2nd name is DIFFERENT! But Spells are SAME!")
    else:
        print("1st and 2nd name is DIFFERENT!")

    # for文
    for cnt in range(3):
        print("[for] count = " + str(cnt))

    # while文
    cnt = 0
    while cnt < 3:
        print("[while] count = " + str(cnt))
        cnt+=1




if __name__ == '__main__':
    main()
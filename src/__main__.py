# 関数の宣言
import flow_controls
import rw_file
import my_class

def main():
    # print
    print("Hello, world!")

    while True:
        menu_string = "\nEnter the following menu number or character.\n1:If-elif-else 2:Loop 3:Match 4:File 5:Class q:Exit\n"
        # 標準入力
        input_str = input(menu_string)
        if not input_str.isdecimal():
            if input_str == "q":
                print("\nGood Bye.\n")
                return
            else:
                continue

        match int(input_str):
            case 1:
                #if-elif-else文
                flow_controls.if_elif_else()
            case 2:
                #for文 while文
                flow_controls.loop()
            case 3:
                #match
                flow_controls.match()
            case 4:
                #file読み書き
                rw_file.rw_file()

            case 5:
                #Class
                my_class.run()
        

if __name__ == '__main__':
    main()
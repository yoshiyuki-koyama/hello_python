import os
def rw_file():
    print("Current Directory:" + os.getcwd())
    input_str = input("Enter the following character or word\nr:read w:write a:append with:with-statement\n")
    match input_str.strip().lower():
        case "r":
            file_name = input("Enter file name\n")
            print("\Read from \"" + file_name + "\"")
            if os.path.isfile(file_name):
                file = open(file_name, "r")
                file_content = file.read()
                print("File Content:")
                print(file_content)
                file.close()
            else:
                print("\"" + file_name + "\" is not file.")

        case "w":
            file_name = input("Enter file name\n")
            print("\nWrite to \"" + file_name + "\"")
            if os.path.exists(file_name):
                answer = input("\"" + file_name + "\" is exist. Do you want overwrite it?(Y/N)\n")
                if not answer.strip().lower() == "y":
                    return
            file = open(file_name, "w")
            file_content = input("Enter any string\n")
            file.write(file_content)
            file.close()
            print("\"" + file_name + "\" has been overwrited")

        case "a":
            file_name = input("Enter file name\n")
            print("\nAppend to \"" + file_name + "\"")
            if os.path.exists(file_name):
                answer = input("\"" + file_name + "\" is exist. Do you want append it?(Y/N)\n")
                if not answer.strip().lower() == "y":
                    return
            file = open(file_name, "a")
            file_content = input("Enter any string\n")
            file.write(file_content)
            file.close()
            print("\"" + file_name + "\"\'s content has been appended")

        case "with":
            print("\nOpen multiple files. (test1.txt , test2.txt, test3.txt)")
            if os.path.exists("test1.txt") or os.path.exists("test2.txt") or os.path.exists("test3.txt"):
                answer = input("\"test1.txt\" or \"test2.txt\" or \"test3.txt\" are exist. Do you want overwrite it?(Y/N)\n")
                if not answer.strip().lower() == "y":
                    return
            with (open("test1.txt", "w") as test1,
                  open("test2.txt", "w") as test2,
                  open("test3.txt", "w") as test3):
                test1.write("abcd")
                test2.write("efgh")
                test3.write("ijkl")
            # 自動でファイルクローズされる
            print("\"test1.txt\", \"test2.txt\", \"test3.txt\" has been overwrited")
        case _:
            print("??????")

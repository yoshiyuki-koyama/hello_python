import os
def rw_file():
    print("Current Directory:" + os.getcwd())
    input_str = input("Enter the following characters\nr:read w:write a:append\n")
    file_name = input("Enter file name\n")
    match input_str.strip().lower():
        case "r":
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
        case _:
            print("??????")

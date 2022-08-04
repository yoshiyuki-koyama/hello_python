def run():
    #インスタンス作成
    my_class = MyClass("dog")
    my_class2 = MyClass("cat")
    my_class.print_name_and_id()
    my_class2.print_name_and_id()
    MyClass.print_class_variable()
    
class MyClass:
    # クラス変数(static)
    class_name = "MyClass"
    class_id_counter = 0
    class_list = []

    # コンストラクタ
    def __init__(self, name: str):
        # クラス変数を明示的に操作するには__class__をつける(?)。class_id_counterの場合__class__をつけないとインスタンスにされたのは整数型(immutable)だから？
        self.id = self.__class__.class_id_counter
        self.name = name
        self.__class__.class_id_counter+=1
        self.class_list.append(name)
        print(self.class_name + " is created. instance id = " + str(self.id) + ". class id counter = " + str(self.class_id_counter))

    def print_name_and_id(self):
         print("Instance name is \"" + self.name + "\". id = " +str(self.id))

    def print_class_variable():
        print("Class name is \"" + __class__.class_name + "\". class id counter = " +str(__class__.class_id_counter))
        print("Instance names list: " + str(__class__.class_list))
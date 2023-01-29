# Как то вечером три разработчика написали 
# три метода класса `SomeClass`, каждый под себя. 
# Методы по сути своей почти одинаковые.
#
# Напишите свой метод `sorted_func`, 
# учитывая особенности всех представленных методов


class SomeClass:
    def __init__(self):
        self.list = [1, 1, 2, 2, 3, 4]

    def sorted_func(self, reverse: bool = False):
        return sorted(self.list, reverse=reverse)


if __name__ == "__main__":
    some_instance = SomeClass()
    print(some_instance.sorted_func())

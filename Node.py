class Node:
    __prev = None
    __forth = None
    __value = None

    def __init__(self, value, forth=None, prev=None):
        self.__value = value
        self.__prev = prev
        self.__forth = forth

    @property
    def value(self):
        return self.__value

    @property
    def forth(self):
        return self.__forth

    @forth.setter
    def forth(self, value):
        self.__forth = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value


if __name__ == "__main__":
    n = Node(2)
    n.prev = 2
    print(n.prev)

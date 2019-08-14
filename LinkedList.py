import Node


class DoublyLinkedList:
    __head = None
    __tail = None
    __size = 0

    def __init__(self, arr=None):
        if arr is None:
            arr = []
        for el in arr:
            self.add_last(el)

    def __str__(self):
        text = []
        cur = self.__head
        while cur is not None:
            text.append(str(cur.value))
            cur = cur.forth
        return f"[{', '.join(text)}]"

    def __repr__(self):
        return f"DoublyLinkedList({self.__str__()})"

    def add_first(self, value):
        new_node = Node.Node(value)
        if self.is_empty:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.forth = self.__head
            self.__head.prev = new_node
            self.__head = new_node
        self.__size += 1

    def add_last(self, value):
        new_node = Node.Node(value)
        if self.is_empty:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.prev = self.__tail
            self.__tail.forth = new_node
            self.__tail = new_node
        self.__size += 1

    def remove_first(self):
        if self.is_empty:
            return None

        value = self.__head.value
        if self.__size == 1:
            self.__head = None
            self.__tail = None
        self.__head = self.__head.forth
        self.__size -= 1
        return value

    def remove_last(self):
        if self.is_empty:
            return None

        value = self.__tail.value
        if self.__size == 1:
            self.__head = None
            self.__tail = None
        self.__tail = self.__tail.prev
        self.__size -= 1
        return value

    def clear(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    @property
    def is_empty(self):
        return self.__size == 0

    @property
    def size(self):
        return self.__size


if __name__ == "__main__":
    l = DoublyLinkedList([2, 3, 1, 7, 0])
    print(l)
    l.remove_first()
    print(l)
    l.remove_first()
    print(l)
    l.add_last("top kek")
    print(l)

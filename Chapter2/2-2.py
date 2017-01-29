
class Node:

    def __init__(self, value):
        self.__next = None
        self.__value = value

    def set_next(self, next):
        self.__next = next

    def get_next(self):
        return self.__next
    next = property(get_next, set_next)

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value
    value = property(get_value, set_value)

class NodeList:

    def __init__(self, head):
        self.__head = head
        self.__count = 1
        self.__tail = head


    def get_head(self):
        return self.__head

    def set_head(self, head):
        self.__head = head
        self.__count = 0
        self.__tail = head

    head = property(get_head, set_head)

    def add_node(self, node):
        if self.__head is None:
            self.set_head(node)
        else:
            self.__count += 1
            self.__tail.next = node
            self.__tail = node

    def get_last_kth_node(self, k):
        i = 0
        node = self.__head
        while i < self.__count - k:
            node = node.next
            i += 1
        return node


    def __str__(self):
        string = ""
        node = self.__head
        while not node is None:
            string = string + ", " + node.value
            node = node.next
        return string

if __name__ == "__main__":
    node_a = Node("aaaa")
    node_list = NodeList(node_a)
    print(node_list)
    node_b = Node("bbbb")
    node_c = Node("cccc")
    node_d = Node("dddd")

    # node_list.head = node_a


    node_list.add_node(node_b)
    node_list.add_node(node_c)
    node_list.add_node(node_d)
    # node_list.add_node(node_c)
    # node_list.add_node(node_d)
    print(node_list)

    node = node_list.get_last_kth_node(1)
    print(node.value)
    node = node_list.get_last_kth_node(2)
    print(node.value)
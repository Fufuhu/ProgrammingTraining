

class Node:

    def __init__(self, data):
        self.__data = data
        self.__next = None


    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next



    def set_data(self, data):
        return self.__data

    def get_data(self):
        return self.__data

    next = property(get_next, set_next)
    data = property(get_data, set_data)

class List:

    def __init__(self):
        self.__head = None

    def set_head(self, head):
        self.__head = head

    def get_head(self):
        return self.__head

    def deduplicate(self):
        list = List()
        node_prev = None
        node = self.head
        node_hash = {}
        while node != None:
            if not node.data in node_hash:
                node_hash[node.data] = True
                node_created = Node(node.data)
                if list.head == None:
                    list.head = node_created
                node_prev = node_created


            node = node.next
        return list

    head = property(get_head, set_head)

if __name__ == "__main__":
    list = List()
    node = Node("test1")
    list.set_head(node)

    node2 = Node("test")
    node.next = node2
    node3 = Node("test")
    node2.next = node3

    node = list.head
    while node != None:
        print(node.data) 
        node = node.next
    
    list_a = list.deduplicate()
    node = list_a.head
    print("******")
    while node != None:
        print(node.data)
        node = node.next
    




class Node:

    def __init__(self, value):
        self.__next = None
        self.__value = value

    next = property(get_next, set_next)
    def set_next(self, next):
        self.__next = next
    
    def get_next(self):
        return self.__next

    value = property(get_value, set_value)
    def set_value(self, value):
        self.__value = value
    
    def get_value(self):
        return self.__value

class List:
    
    
    def __init__(self, head):
        self.__head = head
    
    head = property(get_head, set_head)

    def get_head(self):
        return self.__head
    
    def set_head(self, head):
        self.__head = head



if __name__ == "__main__":


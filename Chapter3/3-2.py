class Stack:
    def __init__(self):
        self.__stack = []
        self.__min_stack = []

    def push(self, value):
        self.__stack = self.__stack + [value]

        if len(self.__min_stack) == 0:
            self.__min_stack = self.__min_stack + [value]
        elif self.__min_stack[len(self.__min_stack) - 1] > value:
            self.__min_stack = self.__min_stack + [value]
        else:
            self.__min_stack = \
                self.__min_stack + [self.__min_stack[len(self.__min_stack)-1]]


    def pop(self):
        if len(self.__stack) == 0:
            return None
        else:
            self.__min_stack.pop()
            return self.__stack.pop()

    def min(self):
        return self.__min_stack[len(self.__min_stack) - 1]


if __name__ == "__main__":
    stack = Stack()
    stack.push(200)
    stack.push(100)
    stack.push(300)
    stack.push(30)
    min = stack.min()
    print("Min:"+str(min))

    value = stack.pop()
    print("Pop Value:"+str(value))

    min = stack.min()
    print("Min(after pop()):"+str(min))
    print("Pop Value:"+ str(stack.pop()))
    print("Pop Value:"+ str(stack.pop()))
    print("Min(after pop() 2:"+ str(stack.pop()))

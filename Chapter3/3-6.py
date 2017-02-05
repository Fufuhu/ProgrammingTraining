import copy

class OrderedStack():

    def __init__(self):
        self.__ordered_stack = []

    def push(self, value):

        stack = []
        # if len(self.__ordered_stack) == 0:
        #     self.__ordered_stack = self.__ordered_stack + [value]
        #     return

        while True:
            if len(self.__ordered_stack) > 0:
                node = self.__ordered_stack.pop()
                if value > node:
                    stack = stack + [value]
                    stack = stack + [node]
                    break
                else:
                    stack = stack + [node]
            else:
                stack = stack + [value]
                break

        while len(stack) > 0:
            self.__ordered_stack = self.__ordered_stack + [stack.pop()]

    def pop(self):
        if self.isEmpty() == False:
            return self.__ordered_stack.pop()
        else:
            return False

    def isEmpty(self):
        return len(self.__ordered_stack) == 0

    def __str__(self):
        return str(self.__ordered_stack)


if __name__ == "__main__":
    stack = OrderedStack()
    print("####push:100")
    stack.push(100)
    print("####push:10")
    stack.push(10)
    print("####push:30")
    stack.push(30)
    print("####push:50")
    stack.push(50)
    print("####push:200")
    stack.push(200)

    print(stack)

    print(str(stack.pop()))
    print(str(stack.pop()))
    print(str(stack.pop()))
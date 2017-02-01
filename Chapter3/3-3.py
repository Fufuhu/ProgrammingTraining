class SetOfStacks:

    limit = 4
    
    def __init__(self):
        stack = []
        self.__stacks = [stack]

    def pop(self):
        if len(self.__stacks) == 0:
            return None
        stack = self.__stacks.pop()
        print("Stacks:"+str(self.__stacks))
        print("Stack:"+str(stack))
        if len(stack) == 0:
            stack = self.__stacks.pop()
        value = stack.pop()
        if len(stack) > 0:
            self.__stacks = self.__stacks + [stack]
        return value


    def push(self, value):
        stack = self.__stacks.pop()
        if len(stack) >= self.limit:
            self.__stacks = self.__stacks + [stack, [value]]
        else:
            stack = stack + [value]
            self.__stacks = self.__stacks + [stack]

        print("Push(stacks):"+str(self.__stacks))
        # for stack in self.__stacks:
        #     if len(stack) < self.limit:
        #         stack = stack + [value]
        #     else:
        #         stack = [value]
        #         self.__stacks = self.__stacks + [stack]
        # self.__stacks = self.__stacks + [stack]
 
if __name__ == "__main__":
    stacks = SetOfStacks()

    stacks.push(4)
    stacks.push(2)
    stacks.push(3)
    stacks.push(4)
    stacks.push(5)

    print(str(stacks.pop()))
    print(str(stacks.pop()))
    print(str(stacks.pop()))
    print(str(stacks.pop()))
    print(str(stacks.pop()))
    print(str(stacks.pop()))



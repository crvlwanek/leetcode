class MinStack:

    def __init__(self):
        self.__stack = []
        self.__min = []

    def push(self, val: int) -> None:
        if not self.__min or self.__min[-1][0] > val:
            self.__min.append((val, len(self.__stack)))
        self.__stack.append(val)

    def pop(self) -> None:
        self.__stack.pop()
        if len(self.__stack) == self.__min[-1][1]:
            self.__min.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__min[-1][0]


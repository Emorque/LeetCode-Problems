class MyQueue:

    def __init__(self):
        self.popStack = []
        self.pushStack = []

    def push(self, x: int) -> None:
        self.pushStack.append(x)

    def pop(self) -> int:
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
            return self.popStack.pop()
        else:
            return self.popStack.pop()

    def peek(self) -> int:
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
            return self.popStack[-1]
        else:
            return self.popStack[-1]

    def empty(self) -> bool:
        return (not self.popStack) and (not self.pushStack)
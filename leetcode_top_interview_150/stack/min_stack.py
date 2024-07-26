class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)

        if not self.min_stk or val <= self.min_stk[-1]:
            self.min_stk.append(val)

    def pop(self) -> None:
        if self.stk:
            removed = self.stk.pop()
            if removed == self.min_stk[-1]:
                self.min_stk.pop()

    def top(self) -> int:
        if self.stk:
            return self.stk[-1]

    def getMin(self) -> int:
        if self.min_stk:
            return self.min_stk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

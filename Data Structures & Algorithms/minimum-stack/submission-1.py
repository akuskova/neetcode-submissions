class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mins = min(val,self.mins)
        
    def pop(self) -> None:
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

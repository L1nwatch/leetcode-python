class CQueue:

    def __init__(self):
        self.stack_in = list()
        self.stack_out = list()

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)


    def deleteHead(self) -> int:
        if len(self.stack_out) > 0:
            return self.stack_out.pop()
        else:
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())
            if len(self.stack_out) > 0:
                return self.stack_out.pop()
            else:
                return -1



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
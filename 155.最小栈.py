#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.min = None
        self.stack = list()

    def push(self, val: int) -> None:
        if self.min is None:
            self.min = val
        elif self.min > val:
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        value = self.stack.pop()
        if len(self.stack) == 0:
            self.min = None
        elif self.min == value:
            self.min = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

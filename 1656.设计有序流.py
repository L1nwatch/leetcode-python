#
# @lc app=leetcode.cn id=1656 lang=python3
#
# [1656] 设计有序流
#

# @lc code=start
class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None]*n
        self.point = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value
        answer = list()
        for i in range(self.point, self.n):
            if (x := self.stream[i]) is not None:
                answer.append(x)
                self.point += 1
            else:
                break
        return answer

        # Your OrderedStream object will be instantiated and called as such:
        # obj = OrderedStream(n)
        # param_1 = obj.insert(idKey,value)
# @lc code=end

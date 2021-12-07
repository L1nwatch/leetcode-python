#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#

# @lc code=start
class RecentCounter:

    def __init__(self):
        self.request = list()

    def ping(self, t: int) -> int:
        self.request.append(t)
        index = 0
        while index < len(self.request):
            if self.request[index] >= t-3000:
                break
            index += 1

        self.request = self.request[index:]
        return len(self.request)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

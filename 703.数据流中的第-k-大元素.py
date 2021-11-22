#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#

# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        self.length = len(nums)

    def add(self, val: int) -> int:
        if self.length == 0:
            self.length += 1
            self.nums.append(val)
        elif val > self.nums[-1]:
            self.nums.append(val)
            self.length += 1
        else:
            for i in range(self.length):
                if self.nums[i] >= val:
                    self.nums.insert(i, val)
                    self.length += 1
                    break
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

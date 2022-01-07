#
# @lc app=leetcode.cn id=1437 lang=python3
#
# [1437] 是否所有 1 都至少相隔 k 个元素
#

# @lc code=start
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        step = None
        for num in nums:
            if num == 0 and step is None:
                continue
            elif num == 1 and step is None:
                step = 0
            elif num == 1 and step is not None:
                if step < k:
                    return False
                step = 0
            elif num == 0 and step is not None:
                step += 1
        return True


# @lc code=end

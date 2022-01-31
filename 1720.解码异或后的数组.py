#
# @lc app=leetcode.cn id=1720 lang=python3
#
# [1720] 解码异或后的数组
#

# @lc code=start
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for num in encoded:
            arr.append(num^arr[-1])
        return arr
# @lc code=end


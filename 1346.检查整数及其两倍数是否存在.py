#
# @lc app=leetcode.cn id=1346 lang=python3
#
# [1346] 检查整数及其两倍数是否存在
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count = 0
        for num in arr:
            if num == 0:
                count += 1
        if count >= 2:
            return True
        arr = set(arr)
        for num in arr:
            if num * 2 in arr and num != 0:
                return True
        return False
# @lc code=end


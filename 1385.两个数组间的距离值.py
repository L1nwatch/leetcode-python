#
# @lc app=leetcode.cn id=1385 lang=python3
#
# [1385] 两个数组间的距离值
#

# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        answer = 0
        for num in arr1:
            for target in arr2:
                if abs(num-target) <= d:
                    break
            else:
                answer += 1
        return answer
# @lc code=end


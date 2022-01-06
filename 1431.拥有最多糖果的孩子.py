#
# @lc app=leetcode.cn id=1431 lang=python3
#
# [1431] 拥有最多糖果的孩子
#

# @lc code=start


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        answer = list()
        for candy in candies:
            if candy + extraCandies >= max_candies:
                answer.append(True)
            else:
                answer.append(False)
        return answer
# @lc code=end

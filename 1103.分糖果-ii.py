#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        answer = [0 for _ in range(num_people)]
        n = 1
        index = 0
        while True:
            if n < candies:
                answer[index] += n
                candies -= n
                n += 1
                index = (index+1) % num_people
            else:
                answer[index] += candies
                break
        return answer
# @lc code=end

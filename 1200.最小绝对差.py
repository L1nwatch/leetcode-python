#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        answer = list()
        import sys
        min_minus = sys.maxsize
        for index in range(len(arr)-1):
            minus = arr[index+1]-arr[index]
            if min_minus < minus:
                pass
            elif min_minus == minus:
                answer.append([arr[index], arr[index+1]])
            elif min_minus > minus:
                min_minus = minus
                answer = [[arr[index], arr[index+1]]]
        return answer
# @lc code=end

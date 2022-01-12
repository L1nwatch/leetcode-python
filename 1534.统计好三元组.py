#
# @lc app=leetcode.cn id=1534 lang=python3
#
# [1534] 统计好三元组
#

# @lc code=start
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        answer = 0
        length = len(arr)
        for i in range(length):
            for j in range(i+1, length):
                if abs(arr[i]-arr[j]) <= a:
                    for k in range(j+1, length):
                        if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                            answer += 1
        return answer

# @lc code=end

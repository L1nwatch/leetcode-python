#
# @lc app=leetcode.cn id=1710 lang=python3
#
# [1710] 卡车上的最大单元数
#

# @lc code=start
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        answer = 0
        boxTypes = sorted(boxTypes,key=lambda x:x[1],reverse=True)
        for box in boxTypes:
            if truckSize > box[0]:
                truckSize -= box[0]
                answer += box[0] * box[1]
            else:
                answer += box[1] * truckSize
                break
        return answer
# @lc code=end


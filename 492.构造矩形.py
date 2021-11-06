#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area == 1:
            return [1,1]

        result = list()
        for w in range(1,area//2+1):
            l = area / w
            if not l.is_integer():
                continue
            result.append([int(l),w])
        
        abs_min = area
        answer = result[0]
        for each_result in result:
            abs_this = abs(each_result[0]-each_result[1])
            if abs_this < abs_min:
                answer = each_result
                abs_min=abs_this
        return answer
# @lc code=end


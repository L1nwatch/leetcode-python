#
# @lc app=leetcode.cn id=1694 lang=python3
#
# [1694] 重新格式化电话号码
#

# @lc code=start
class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ","")
        number = number.replace("-","")
        answer = list()
        length = len(number)
        i = 0
        while i < length:
            if length - i == 4:
                answer.append(number[-4:-2])
                answer.append(number[-2:])
                break
            elif length - i == 3:
                answer.append(number[-3:])
                break
            elif length - i == 2:
                answer.append(number[-2:])
                break
            else:
                answer.append(number[i:i+3])
                i += 3
        return "-".join(answer)
# @lc code=end


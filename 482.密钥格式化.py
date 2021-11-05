#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = list()
        count = 0
        for each_char in s[::-1]:
            if each_char == "-":
                continue
            each_char = each_char.upper()
            count += 1
            if count == 1:
                result.append(each_char)
            elif 1 < count <= k:
                result[-1] = each_char + result[-1]
            if count == k:
                count = 0
        result = reversed(result)
        return "-".join(result)
# @lc code=end

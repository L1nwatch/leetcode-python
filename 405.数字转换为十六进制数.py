#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        map_dict = {
            0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"
        }
        if num == 0:
            return "0"

        if num < 0:
            num += 2**32

        string = str()
        while num != 0:
            string = map_dict[num % 16] + string
            num //= 16
        return string
# @lc code=end

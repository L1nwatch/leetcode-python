#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = list()
        for hour in range(12):
            bin_hour_1 = bin(hour).count("1")
            for minute in range(60):
                if bin_hour_1 + bin(minute).count("1") == turnedOn:
                    result.append(f"{hour}:{minute:0>2d}")
        return result
# @lc code=end

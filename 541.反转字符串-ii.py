#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        times = len(s)//(2*k)
        for i in range(times):
            s = s[:i*2*k] + s[i*2*k:i*2*k+k][::-1] + s[i*2*k+k:]
        index = (len(s)//(2*k))*2*k
        left_char_num = len(s)-index
        if 0 < left_char_num < k:
            s = s[:-left_char_num] + s[-left_char_num:][::-1]
        elif k <= left_char_num < 2*k:
            s = s[:index] + s[index:index+k][::-1]+s[index+k:]

        return s


# @lc code=end

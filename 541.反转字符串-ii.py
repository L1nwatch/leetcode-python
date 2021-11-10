#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # deal all 2k string
        # deal with len(s) - 2k*n string


        slow, fast = 0, 0
        while fast < len(s):
            if fast-slow == 2*k-1:
                s = s[:slow] + s[slow:slow+k][::-1] + s[slow+k:]
                slow = fast
                continue

            fast += 1
            left_char_num = len(s)-1-fast

            if left_char_num < k:
                s = s[:fast+1]+s[fast+1:len(s)][::-1]
                break
            elif k <= left_char_num < 2*k:
                s = s[:fast+1] + s[fast+1:fast+k+1][::-1]+s[fast+k+1:]
                break


        return s


# @lc code=end

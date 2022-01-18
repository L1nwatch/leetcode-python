#
# @lc app=leetcode.cn id=1566 lang=python3
#
# [1566] 重复至少 K 次且长度为 M 的模式
#

# @lc code=start
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        arr = ",".join([str(x) for x in arr])+","
        print(arr)
        import re
        if k == 1:
            result = re.findall(r"(\d{"+str(m)+"})", arr)
        else:
            result = re.findall(r"((\d+,){"+str(m)+r"})\1{"+str(k-1)+"}", arr)
        return len(result) >= 1
# @lc code=end

#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#

# @lc code=start
class Solution:
    def sort_by_one_count(self,num):
        return (bin(num).count("1"),num)

    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr,key=lambda x: self.sort_by_one_count(x))
# @lc code=end


#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 有序数组中出现次数超过25%的元素
#

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        import bisect
        length = len(arr)
        span = length // 4 + 1
        for i in range(0, length, span):
            iter_l = bisect.bisect_left(arr, arr[i])
            iter_r = bisect.bisect_right(arr, arr[i])
            if iter_r - iter_l >= span:
                return arr[i]
        return -1


# @lc code=end
        count = dict()
        length = len(arr)//4
        for num in arr:
            count[num] = count.get(num, 0)+1
            if count[num] > length:
                return num

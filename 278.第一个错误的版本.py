#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low < high:
            middle = low + (high-low)//2
            if isBadVersion(middle):
                high = middle
            else:
                low = middle+1
        return low

# @lc code=end

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low < high:
            middle = low + (high-low)//2
            result = isBadVersion(middle)
            if result:
                high = middle
            else:
                low = middle + 1
        return low
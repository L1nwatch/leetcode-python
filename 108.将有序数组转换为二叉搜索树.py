#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) < 1:
            return None
        root = TreeNode()
        middle_index = len(nums)//2
        root.val = nums[middle_index]
        root.left = self.sortedArrayToBST(nums[:middle_index])
        root.right = self.sortedArrayToBST(nums[middle_index+1:])
        return root

# @lc code=end

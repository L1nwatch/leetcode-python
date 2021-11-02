#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        left_leaves_sum = 0
        if root:
            if root.left:
                if root.left.left or root.left.right:
                    left_leaves_sum += self.sumOfLeftLeaves(root.left)
                else:
                    left_leaves_sum += root.left.val
            if root.right:
                left_leaves_sum += self.sumOfLeftLeaves(root.right)
        return left_leaves_sum
# @lc code=end


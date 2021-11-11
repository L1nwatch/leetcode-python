#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def max_depth(self, tree_node: TreeNode) -> int:
        if not tree_node:
            return 0
        left_depth = self.max_depth(tree_node.left)
        right_depth = self.max_depth(tree_node.right)
        self.answer = max(self.answer, left_depth+right_depth+1)
        return max(left_depth, right_depth)+1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.answer = 1
        self.max_depth(root)
        return self.answer - 1
# @lc code=end

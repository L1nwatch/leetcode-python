#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, tree_node: TreeNode) -> int:
        if not tree_node:
            return 0
        left_sum = self.dfs(tree_node.left)
        right_sum = self.dfs(tree_node.right)
        self.result.append(abs(left_sum-right_sum))
        return left_sum + right_sum + tree_node.val

    def findTilt(self, root: TreeNode) -> int:
        self.result = list()
        self.dfs(root)

        return sum(self.result)
# @lc code=end

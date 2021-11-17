#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, tree_1: TreeNode, tree_2: TreeNode) -> TreeNode:
        if not tree_1 and not tree_2:
            return None
        if tree_1 and tree_2:
            tree_1.val += tree_2.val
            tree_1.left = self.dfs(tree_1.left, tree_2.left)
            tree_1.right = self.dfs(tree_1.right, tree_2.right)
            return tree_1
        elif tree_1:
            return tree_1
        elif tree_2:
            return tree_2

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        root = self.dfs(root1, root2)
        return root
# @lc code=end

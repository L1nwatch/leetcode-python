#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: TreeNode, path: str) -> None:
        if node:
            path += str(node.val)
            if node.left is None and node.right is None:
                self.paths.append(path)
            else:
                path += "->"
                self.dfs(node.left, path)
                self.dfs(node.right, path)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = list()
        self.dfs(root, str())
        return self.paths

# @lc code=end

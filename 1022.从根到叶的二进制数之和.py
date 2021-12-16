#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, treenode: TreeNode, path: str) -> None:
        if treenode:
            path = path+str(treenode.val)
            if treenode.left or treenode.right:
                self.dfs(treenode.left, path)
                self.dfs(treenode.right, path)
            else:
                self.answer += int(path, 2)

    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.answer = 0
        self.dfs(root, "")
        return self.answer
# @lc code=end

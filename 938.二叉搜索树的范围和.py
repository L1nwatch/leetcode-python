#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, treenode: TreeNode):
        if treenode:
            if self.low <= treenode.val <= self.high:
                self.answer += treenode.val
                self.dfs(treenode.left)
                self.dfs(treenode.right)
            elif treenode.val < self.low:
                self.dfs(treenode.right)
            elif treenode.val > self.high:
                self.dfs(treenode.left)

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.answer = 0
        self.low = low
        self.high = high
        self.dfs(root)
        return self.answer
# @lc code=end

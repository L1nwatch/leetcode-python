#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _isSymmetric(self, tree1: TreeNode, tree2: TreeNode) -> bool:
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        if tree1.val != tree2.val:
            return False
        return self._isSymmetric(tree1.left, tree2.right) and self._isSymmetric(tree1.right, tree2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self._isSymmetric(root, root)


# @lc code=end

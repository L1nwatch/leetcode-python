#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        result, stack = list(), list()
        if root:
            stack.append(root)
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node:
                if current_node.right:
                    stack.append(current_node.right)
                stack.append(current_node)
                stack.append(None)
                if current_node.left:
                    stack.append(current_node.left)
            else:
                current_node = stack.pop()
                result.append(current_node.val)

        minus = result[1]-result[0]
        for i in range(2, len(result)):
            minus = min(result[i]-result[i-1], minus)
        return minus
# @lc code=end

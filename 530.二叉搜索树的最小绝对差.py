#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        answer = 10 ** 5
        pre_val = -1
        result = list()
        stack = list()
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
                if pre_val == -1:
                    pre_val = current_node.val
                else:
                    answer = min(answer,current_node.val - pre_val)
                    pre_val = current_node.val

        return answer
# @lc code=end


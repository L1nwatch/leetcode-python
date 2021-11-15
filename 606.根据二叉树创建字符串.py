#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result,stack = list(),list()
        if root:
            stack.append(root)
        while len(stack) > 0:
            current_node = stack.pop()
            if type(current_node) is TreeNode:
                if current_node.right:
                    stack.append(")")
                    stack.append(current_node.right)
                    stack.append("(")
                
                if current_node.left:
                    stack.append(")")
                    stack.append(current_node.left)
                    stack.append("(")
                elif current_node.right:
                    stack.append("()")

                stack.append(current_node)
                stack.append(None)
            elif type(current_node) is str:
                result.append(current_node)
            else:
                current_node = stack.pop()
                result.append(str(current_node.val))
        return "".join(result)
# @lc code=end


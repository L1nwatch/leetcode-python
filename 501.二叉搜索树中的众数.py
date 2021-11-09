#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        count = dict()
        stack = list()
        if root:
            stack.append(root)
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node:
                if current_node.right:
                    stack.append(current_node.right)
                if current_node.left:
                    stack.append(current_node.left)
                stack.append(current_node)
                stack.append(None)
            else:
                current_node = stack.pop()
                count[current_node.val] = count.get(current_node.val, 0) + 1

        result = list()
        max_count = max(count.values())
        for each_val,each_count in count.items():
            if each_count == max_count:
                result.append(each_val)
        return result
# @lc code=end

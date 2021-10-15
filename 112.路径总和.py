#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_sum(self, root: TreeNode) -> list:
        result = list()
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        total_list = list()
        total_list.extend(self.get_sum(root.left))
        total_list.extend(self.get_sum(root.right))
        for each_sum in total_list:
            result.append(each_sum+root.val)
        return result

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        total_list = list()
        total_list.extend(self.get_sum(root.left))
        total_list.extend(self.get_sum(root.right))
        for each_sum in total_list:
            if each_sum + root.val == targetSum:
                return True
        if len(total_list) == 0 and root.val == targetSum:
            return True
        return False


# @lc code=end

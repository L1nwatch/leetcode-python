#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, tree_node: TreeNode, level: int):
        if not tree_node:
            return None
        if level < len(self.count):
            self.count[level] += tree_node.val
        else:
            self.count.append(tree_node.val)
        self.nums[level] = self.nums.get(level, 0)+1
        self.dfs(tree_node.left, level+1)
        self.dfs(tree_node.right, level+1)

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.count = list()
        self.nums = dict()
        self.dfs(root, 0)
        return [self.count[i]/self.nums[i] for i in range(len(self.count))]

# @lc code=end

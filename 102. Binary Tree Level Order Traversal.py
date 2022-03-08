# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        answer = list()
        from collections import deque
        next_level_list = [[root]]
        while len(next_level_list) > 0:
            level_list = next_level_list.pop()
            next_level = list()
            this_level_node = list()
            for each_node in level_list:
                if not each_node:
                    continue
                this_level_node.append(each_node.val)
                if each_node.left:
                    next_level.append(each_node.left)
                if each_node.right:
                    next_level.append(each_node.right)
            if len(this_level_node) > 0:
                answer.append(this_level_node)
            if len(next_level) > 0:
                next_level_list.append(next_level)

        return answer
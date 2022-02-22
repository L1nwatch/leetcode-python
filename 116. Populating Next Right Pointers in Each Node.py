"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def dfs(self,current_node, parent_node, position):
        if not current_node:
            return
        if position == "root":
            current_node.next = None
        elif position == "left":
            current_node.next = parent_node.right
        elif position == "right":
            current_node.next = parent_node.next.left if parent_node.next else None

        self.dfs(current_node.left,current_node,"left")
        self.dfs(current_node.right,current_node,"right")

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.dfs(root,None,"root")
        return root
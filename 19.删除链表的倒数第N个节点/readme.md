# Question

```shell
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_map, i = {1: head}, 1
        cur_node = head
        while cur_node.next != None:
            i += 1
            node_map[i] = cur_node.next
            cur_node = cur_node.next

        # 删除第一个节点
        if i == n:
            head = node_map[2] if i >= 2 else None
        # 删除最后一个节点
        elif n == 1:
            node_map[i - n].next = None
        # 删除中间一个节点
        else:
            node_map[i - n].next = node_map[i - n + 2]

        return head
```

跑出来的结果：

```shell
执行用时 :40 ms, 在所有 Python3 提交中击败了96.40%的用户
内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.53%的用户
```

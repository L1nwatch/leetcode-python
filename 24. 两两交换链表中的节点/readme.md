# Question

```shell
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        l_point, r_point, temp_point = head, head.next, head
        while r_point:
            l_point.next = r_point.next
            r_point.next = l_point
            if l_point == head:
                head = r_point
                temp_point = l_point
            else:
                temp_point.next = r_point
                temp_point = l_point
            if not l_point.next:
                break
            l_point = l_point.next
            r_point = l_point.next

        return head
```

跑出来的结果：

```shell
执行结果：通过 显示详情
执行用时 :40 ms, 在所有 Python3 提交中击败了71.40%的用户
内存消耗 :13.5 MB, 在所有 Python3 提交中击败了6.25%的用户
```
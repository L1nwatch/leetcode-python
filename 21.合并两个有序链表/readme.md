# Question

```shell
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = head_result = None
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            if l1.val >= l2.val:
                result = head_result = l2
                l2 = l2.next
            else:
                result = head_result = l1
                l1 = l1.next
        while l1 is not None and l2 is not None:
            if l1.val >= l2.val:
                result.next = l2
                l2 = l2.next
            else:
                result.next = l1
                l1 = l1.next
            result = result.next
        if l1 is not None:
            result.next = l1
        if l2 is not None:
            result.next = l2
        return head_result

```

跑出来的结果：

```shell
执行用时 :44 ms, 在所有 Python3 提交中击败了96.65%的用户
内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.66%的用户
```

# Question

```shell
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 得到第一个数
        num1 = str(l1.val)
        while l1.next:
            l1 = l1.next
            num1 += str(l1.val)

        # 得到第二个数
        num2 = str(l2.val)
        while l2.next:
            l2 = l2.next
            num2 += str(l2.val)

        num1 = num1[::-1]
        num2 = num2[::-1]
        # 相加，返回结果
        result = str(int(num1) + int(num2))
        result = result[::-1]
        root_list = ListNode(int(result[0]))
        last_list = root_list
        for i in range(1, len(result)):
            last_list.next = ListNode(int(result[i]))
            last_list = last_list.next
        return root_list
```

跑出来的结果：

```shell
执行用时 :104 ms, 在所有 Python3 提交中击败了66.66%的用户
内存消耗 :13.2 MB, 在所有 Python3 提交中击败了53.54%的用户
```

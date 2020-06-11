# Question

```shell
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer1

```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 1:
            return lists[0]

        data_list = list()
        result = header = None
        for i, each_list_node in enumerate(lists):
            if each_list_node:
                data_list.append((i, each_list_node.val))
        data_list = sorted(data_list, key=lambda x: x[1])
        while len(data_list) > 0:
            low_index = data_list.pop(0)[0]
            if not header:
                result = header = lists[low_index]
            else:
                result.next = lists[low_index]
                result = result.next
            lists[low_index] = lists[low_index].next
            if lists[low_index]:
                len_data_list = len(data_list)
                for i, each_data in enumerate(data_list):
                    if lists[low_index].val <= each_data[1]:
                        data_list.insert(i, (low_index, lists[low_index].val))
                        break
                    if i == len_data_list - 1:
                        data_list.append((low_index, lists[low_index].val))
                        break
        return header

```

跑出来的结果：

```shell
执行结果：通过 显示详情
执行用时 :96 ms, 在所有 Python3 提交中击败了65.00%的用户
内存消耗 :17 MB, 在所有 Python3 提交中击败了7.14%的用户
```

# My Answer2

```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 1:
            return lists[0]
        result = header = None
        while True:
            low_index = None
            data_list = list()
            flag = False
            for i, each_list_node in enumerate(lists):
                if each_list_node:
                    data_list.append((i, each_list_node.val))
                    flag = True
            data_list = sorted(data_list, key=lambda x: x[1])
            if not flag:
                break
            low_index = data_list[0][0]
            if not header:
                result = header = lists[low_index]
            else:
                result.next = lists[low_index]
                result = result.next
            lists[low_index] = lists[low_index].next
        return header
```

跑出来的结果：

```shell
超出时间限制
```

# My Answer3

```python

class Solution1:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 1:
            return lists[0]
        result = header = None
        while [True for each_node in lists if each_node].count(True) >= 1:
            low_index = None
            for i, each_list_node in enumerate(lists):
                # not empty point
                if each_list_node:
                    if low_index is None:
                        low_index = i
                        continue
                    if lists[low_index].val > each_list_node.val:
                        low_index = i
            if not header:
                result = header = lists[low_index]
            else:
                result.next = lists[low_index]
                result = result.next
            lists[low_index] = lists[low_index].next
        return header
```

跑出来的结果：

```shell
超出时间限制
```

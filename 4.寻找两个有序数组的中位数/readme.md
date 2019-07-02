# Question

```shell
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        length = len(nums1)
        if length % 2 == 0:
            return (nums1[length // 2] + nums1[(length - 1) // 2]) / 2.0
        else:
            return float(nums1[length // 2])
```

跑出来的结果：

```shell
执行用时 :92 ms, 在所有 Python3 提交中击败了42.88%的用户
内存消耗 :13.3 MB, 在所有 Python3 提交中击败了82.18%的用户
```

# Question

```shell
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        length = len(nums)
        result = 2 ** 31
        for i in range(length - 2):
            l, r = i + 1, length - 1
            while l < r:
                this_sum = nums[i] + nums[l] + nums[r]
                if this_sum < target:
                    l += 1
                    while nums[l] == nums[l - 1] and (l + 1) < length:
                        l += 1
                    if abs(target - this_sum) < abs(target - result):
                        result = this_sum
                elif this_sum > target:
                    r -= 1
                    while nums[r] == nums[r + 1] and (r - 1) > i:
                        r -= 1
                    if abs(target - this_sum) < abs(target - result):
                        result = this_sum
                else:
                    return target
        return result
```

跑出来的结果：

```shell
执行用时 :152 ms, 在所有 Python3 提交中击败了59.17%的用户
内存消耗 :13.1 MB, 在所有 Python3 提交中击败了83.30%的用户
```

# Question

```shell
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        length = len(nums)
        result_list = list()
        if length > 0 and nums[0] <= 0:
            for i in range(length - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                l, r = i + 1, length - 1
                while l < r:
                    this_sum = nums[i] + nums[l] + nums[r]
                    if this_sum < 0:
                        l += 1
                        while nums[l] == nums[l - 1] and (l + 1) < length:
                            l += 1
                    elif this_sum > 0:
                        r -= 1
                        while nums[r] == nums[r + 1] and (r - 1) > i:
                            r -= 1
                    else:
                        result_list.append((nums[i], nums[l], nums[r]))
                        l += 1
                        r -= 1
                        while nums[l] == nums[l - 1] and (l + 1) < length:
                            l += 1
                        while nums[r] == nums[r + 1] and (r - 1) > i:
                            r -= 1
        return result_list
```

跑出来的结果：

```shell
执行用时 :1616 ms, 在所有 Python3 提交中击败了29.60%的用户
内存消耗 :16.4 MB, 在所有 Python3 提交中击败了98.50%的用户
```

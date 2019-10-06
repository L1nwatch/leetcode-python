# Question

```shell
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                c = b + 1
                d = len(nums) - 1
                while c != d:
                    this_list = (nums[a], nums[b], nums[c], nums[d])
                    sum_this_list = sum(this_list)
                    if sum_this_list == target:
                        result.add(this_list)
                        c += 1
                    elif sum_this_list > target:
                        d -= 1
                    elif sum_this_list < target:
                        c += 1
        return list([list(i) for i in result])
```

跑出来的结果：

```shell
执行用时 :1512 ms, 在所有 Python3 提交中击败了32.69%的用户
内存消耗 :13.8 MB, 在所有 Python3 提交中击败了11.17%的用户
```

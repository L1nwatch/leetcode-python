# Question

```shell
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip(" ")
        result = ""
        # with "-" or "+"
        if str.startswith("-") or str.startswith("+"):
            result += str[0]
            str = str[1:]
        for each_num in str:
            if each_num in string.digits:
                result += each_num
            else:
                break
        num = result.lstrip("-+")
        if len(num) <= 0 or num[0] not in string.digits:
            return 0
        result = int(result)
        if abs(result) > (2 ** 31 - 1):
            return -2 ** 31 if result < 0 else (2 ** 31 - 1)
        return result
```

跑出来的结果：

```shell
执行用时 :76 ms, 在所有 Python3 提交中击败了27.64%的用户
内存消耗 :13.1 MB, 在所有 Python3 提交中击败了95.13%的用户
```

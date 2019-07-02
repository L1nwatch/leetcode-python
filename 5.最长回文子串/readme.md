# Question

```shell
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length <= 1:
            return s
        dp = [[False for l in range(length)] for r in range(length)]
        max_length = 0
        result = s[0]
        for r in range(1, length):
            for l in range(r):
                if s[l] == s[r] and ((r - l) == 1 or (r - l) == 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    if (r - l + 1) > max_length:
                        max_length = r - l + 1
                        result = s[l:r + 1]
        return result
```

## 超时答案

100 / 103 个通过测试用例

```python
class Solution:
    def is_huiwen(self,string):
        return string == string[::-1]

    def longestPalindrome(self, s: str) -> str:
        max_s = ""
        for i in range(len(s)):
            temp_s = ""
            temp_max = ""
            for j in range(i,len(s)):
                temp_s += s[j]
                if self.is_huiwen(temp_s) and len(temp_s) > len(temp_max):
                    temp_max = temp_s
            if len(temp_max) > len(max_s):
                max_s = temp_max
        return max_s
```

跑出来的结果：

```shell
执行用时 :5144 ms, 在所有 Python3 提交中击败了23.67%的用户
内存消耗 :21.6 MB, 在所有 Python3 提交中击败了12.81%的用户
```

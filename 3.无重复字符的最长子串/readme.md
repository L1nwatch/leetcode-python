# Question

```shell
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            this_set = set()
            for j in range(i,len(s)):
                if s[j] not in this_set:
                    this_set.add(s[j])
                else:
                    break
            max_length = len(this_set) if len(this_set) > max_length else max_length
        return max_length
```

跑出来的结果：

```shell
执行用时 :652 ms, 在所有 Python3 提交中击败了13.59%的用户
内存消耗 :13.2 MB, 在所有 Python3 提交中击败了53.54%的用户
```

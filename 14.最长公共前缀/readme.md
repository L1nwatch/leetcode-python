# Question

```shell
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = str()
        if len(strs) <= 0:
            return result
        length_list = [len(x) for x in strs]
        min_length = min(length_list)
        index = length_list.index(min_length)
        this_str = strs[index]
        for i,each_char in enumerate(this_str):
            for each_str in strs:
                if each_char != each_str[i]:
                    return result
            result += each_char
        return result
```

跑出来的结果：

```shell
执行用时 :40 ms, 在所有 Python3 提交中击败了98.79%的用户
内存消耗 :13 MB, 在所有 Python3 提交中击败了96.58%的用户
```

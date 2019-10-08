# Question

```shell
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for each_char in s:
            if each_char in ("(", "{", "["):
                stack.append(each_char)
            elif each_char in (")", "}", "]"):
                if len(stack) <= 0:
                    return False
                this_char = stack.pop(-1)
                if (each_char == ")" and this_char != "(") or (each_char == "}" and this_char != "{") or (
                        each_char == "]" and this_char != "["):
                    return False
        return True if len(stack) == 0 else False
```

跑出来的结果：

```shell
执行用时 :36 ms, 在所有 Python3 提交中击败了98.63%的用户
内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.51%的用户
```

# Question

```shell
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

抄题解的，闭包数

```python
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return [""]
        answer = list()
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - 1 - i):
                    answer.append("({}){}".format(left, right))
        return answer
```

跑出来的结果：

```shell
抄题解的，闭包数
执行用时 :52 ms, 在所有 Python3 提交中击败了73.84%的用户
内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.03%的用户
```

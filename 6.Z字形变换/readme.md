# Question

```shell
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        list_nums = min(numRows, len(s))
        result = [list() for i in range(list_nums)]
        go_down = True
        x = 0
        for each_char in s:
            if go_down:
                # down
                result[x].append(each_char)
                x += 1
            else:
                # right-top
                result[x].append(each_char)
                x -= 1
            # last_line
            if x == numRows:
                go_down = False  # right_top
                x -= 2
            # first_line
            if x == 0:
                go_down= True
        result_str = ""
        for each_list in result:
            result_str += "".join(each_list)
        return result_str
```

跑出来的结果：

```shell
执行用时 :92 ms, 在所有 Python3 提交中击败了75.13%的用户
内存消耗 :13.1 MB, 在所有 Python3 提交中击败了95.70%的用户
```

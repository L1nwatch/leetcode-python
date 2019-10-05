# Question

```shell
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
```

![图](https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/17_telephone_keypad.png)

```shell
示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

# My Answer

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters_digit_map = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if len(digits) <= 0:
            return digits

        result = list()
        i = 0
        for each_char in letters_digit_map[digits[i]]:
            result.append("{}".format(each_char))
        i += 1

        while i < len(digits):
            temp_result = list()
            for each_result in result:
                for each_char in letters_digit_map[digits[i]]:
                    temp_result.append("{}{}".format(each_result, each_char))
            result = temp_result
            i += 1

        return result
```

跑出来的结果：

```shell
执行用时 :44 ms, 在所有 Python3 提交中击败了85.59%的用户
内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.30%的用户
```

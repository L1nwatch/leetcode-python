#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start
class Solution:
    def get_repeat_list(self, string: str) -> list:
        result = list()
        length = len(string)
        index = 1
        count = 1
        while index <= length:
            if index < length and string[index] == string[index - 1]:
                count += 1
            else:
                result.append(string[index-1]*count)
                count = 1
            index += 1

        return result

    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_list = self.get_repeat_list(name)
        typed_list = self.get_repeat_list(typed)
        if len(name_list) != len(typed_list):
            return False
            
        for x, y in zip(name_list, typed_list):
            if x not in y:
                return False
        return True


# @lc code=end

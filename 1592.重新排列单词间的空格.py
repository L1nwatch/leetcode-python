#
# @lc app=leetcode.cn id=1592 lang=python3
#
# [1592] 重新排列单词间的空格
#

# @lc code=start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        word_list = list()
        word = str()
        space_num = 0
        for char in text:
            if char == " ":
                space_num += 1
                if word != "":
                    word_list.append(word)
                    word = ""
            else:
                word += char
        else:
            if word != "":
                word_list.append(word)

        word_num = len(word_list)
        if word_num <= 1:
            return "".join(word_list) + " "*space_num
        else:
            max_space = space_num // (word_num - 1)
            return (" "*max_space).join(word_list) + " "*(space_num % (word_num-1))


# @lc code=end

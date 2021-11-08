#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = list()
        line_1 = "qwertyuiop"
        line_2 = "asdfghjkl"
        line_3 = "zxcvbnm"
        for each_word in words:
            lower_each_word = each_word.lower()
            search_line = None
            if lower_each_word[0] in line_1:
                search_line = line_1
            elif lower_each_word[0] in line_2:
                search_line = line_2
            elif lower_each_word[0] in line_3:
                search_line = line_3
            
            flag = True
            for each_char in lower_each_word:
                if each_char not in search_line:
                    flag = False
                    break
            if flag:
                result.append(each_word)
        return result
# @lc code=end


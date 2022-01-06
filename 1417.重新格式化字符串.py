#
# @lc app=leetcode.cn id=1417 lang=python3
#
# [1417] 重新格式化字符串
#

# @lc code=start
class Solution:
    def reformat(self, s: str) -> str:
        num = list()
        alphabet = list()
        for char in s:
            if char.isdigit():
                num.append(char)
            else:
                alphabet.append(char)

        length_num = len(num)
        length_alphabet = len(alphabet)
        if abs(length_num-length_alphabet) > 1:
            return ""
        elif length_num == length_alphabet:
            start_list = num
            second_list = alphabet
            not_equal = False
        elif length_num > length_alphabet:
            start_list = num
            second_list = alphabet
            not_equal = True
        elif length_num < length_alphabet:
            start_list = alphabet
            second_list = num
            not_equal = True

        answer = str()
        for x, y in zip(start_list, second_list):
            answer += x
            answer += y
        if not_equal:
            answer += start_list[-1]
        return answer
# @lc code=end

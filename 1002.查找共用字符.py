#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        import collections
        answer = list(words[0])
        for i in range(1, len(words)):
            counter = collections.Counter(words[i])
            remove_list = list()
            for char in answer:
                if char not in counter:
                    remove_list.append(char)
                else:
                    counter[char] -= 1
                    if counter[char] == 0:
                        del counter[char]
            for char in remove_list:
                answer.remove(char)
        return answer
# @lc code=end

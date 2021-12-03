#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

# @lc code=start


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        import collections
        count_s1 = collections.Counter(s1.split(" "))
        count_s2 = collections.Counter(s2.split(" "))
        answer = list()
        for word in count_s1:
            if count_s1[word] == 1 and word not in count_s2:
                answer.append(word)
        for word in count_s2:
            if count_s2[word] == 1 and word not in count_s1:
                answer.append(word)
        return answer
# @lc code=end

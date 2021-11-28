#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        last_e_index = -1
        length = len(s)
        answer = list()
        for i in range(length):
            if s[i] != c and last_e_index == -1:
                answer.append(10**5)
            elif last_e_index != -1 and s[i] != c:
                answer.append(i-last_e_index)
            elif s[i] == c:
                answer.append(0)
                for j in range(last_e_index+1, i):
                    answer[j] = min(answer[j], abs(i-j))
                last_e_index = i
        return answer
# @lc code=end

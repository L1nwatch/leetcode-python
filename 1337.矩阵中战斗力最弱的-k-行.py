#
# @lc app=leetcode.cn id=1337 lang=python3
#
# [1337] 矩阵中战斗力最弱的 K 行
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat = [int("".join([str(x) for x in j]), 2) for j in mat]
        mat = [(x, index) for index, x in enumerate(mat)]
        mat.sort(key=lambda x: x[0])
        answer = list()
        for _ in range(k):
            _, index = mat.pop(0)
            answer.append(index)
        return answer
# @lc code=end

#
# @lc app=leetcode.cn id=1582 lang=python3
#
# [1582] 二进制矩阵中的特殊位置
#

# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        black_row = set()
        black_col = set()
        answer = 0
        length_row = len(mat)
        length_col = len(mat[0])
        for i in range(length_row):
            for j in range(length_col):
                if mat[i][j] == 1:
                    if i not in black_row and j not in black_col:
                        for x in range(i+1, length_row):
                            if mat[x][j] == 1:
                                break
                        else:
                            for x in range(j+1, length_col):
                                if mat[i][x] == 1:
                                    break
                            else:
                                answer += 1
                                print(f"{i}{j}")
                    black_row.add(i)
                    black_col.add(j)
        return answer

# @lc code=end

#
# @lc app=leetcode.cn id=999 lang=python3
#
# [999] 可以被一步捕获的棋子数
#

# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        answer = 0

        r_i, r_j = None, None
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    r_i, r_j = i, j
                    break
            if r_i is not None:
                break

        index = r_i - 1
        while 0 <= index <= len(board)-1:
            if board[index][r_j] == ".":
                index -= 1
            elif board[index][r_j] == "B":
                break
            elif board[index][r_j] == "p":
                answer += 1
                break

        index = r_i + 1
        while 0 <= index <= len(board)-1:
            if board[index][r_j] == ".":
                index += 1
            elif board[index][r_j] == "B":
                break
            elif board[index][r_j] == "p":
                answer += 1
                break

        index = r_j - 1
        while 0 <= index <= len(board[0])-1:
            if board[r_i][index] == ".":
                index -= 1
            elif board[r_i][index] == "B":
                break
            elif board[r_i][index] == "p":
                answer += 1
                break

        index = r_j + 1
        while 0 <= index <= len(board[0])-1:
            if board[r_i][index] == ".":
                index += 1
            elif board[r_i][index] == "B":
                break
            elif board[r_i][index] == "p":
                answer += 1
                break

        return answer

# @lc code=end

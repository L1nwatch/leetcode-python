#
# @lc app=leetcode.cn id=1275 lang=python3
#
# [1275] 找出井字棋的获胜者
#

# @lc code=start
class Solution:
    def is_this_user_win(self, moves: list) -> bool:
        row_count = {0: 0, 1: 0, 2: 0}
        col_count = {0: 0, 1: 0, 2: 0}
        for x, y in moves:
            row_count[x] += 1
            col_count[y] += 1
        if 3 in row_count.values() or 3 in col_count.values():
            return True
        elif [0, 0] in moves and [1, 1] in moves and [2, 2] in moves:
            return True
        elif [2, 0] in moves and [1, 1] in moves and [0, 2] in moves:
            return True
        else:
            return False

    def tictactoe(self, moves: List[List[int]]) -> str:
        x_moves = list()
        y_moves = list()
        for index in range(len(moves)):
            if index % 2 == 0:
                x_moves.append(moves[index])
            else:
                y_moves.append(moves[index])

        if self.is_this_user_win(x_moves):
            return "A"
        elif len(moves) == 9:
            return "Draw"
        elif self.is_this_user_win(y_moves):
            return "B"
        else:
            return "Pending"


# @lc code=end

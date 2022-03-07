#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        answer = set()
        import collections
        deque = collections.deque()
        deque.append([sr, sc])
        rows, cols = len(image), len(image[0])
        while len(deque) > 0:
            x, y = deque.popleft()
            if image[x][y] == image[sr][sc]:
                answer.add((x, y))
                for i, j in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                    if 0 <= i < rows and 0 <= j < cols and (i, j) not in answer and image[i][j] == image[sr][sc]:
                        deque.append([i, j])

        for i, j in answer:
            image[i][j] = newColor
        return image

# @lc code=end
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row,column = len(image),len(image[0])

        position = [(0,1),(0,-1),(1,0),(-1,0)]
        done_point = set()
        point_list = [(sr,sc)]
        while len(point_list) > 0:
            r,c = point_list.pop()
            for move_x,move_y in position:
                new_x,new_y = r+move_x,c+move_y
                if 0 <= new_x < row and 0 <= new_y< column and image[new_x][new_y] == image[r][c] and (new_x,new_y) not in done_point:
                    point_list.append((new_x,new_y))
            image[r][c] = newColor
            done_point.add((r,c))
        return image

class Solution3:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m,n = len(image),len(image[0])
        from copy import deepcopy
        answer = deepcopy(image)

        seen = set()
        from collections import deque
        points = deque()
        points.append((sr,sc))
        answer[sr][sc] = newColor
        while points:
            x,y = points.pop()
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0 <= i < m and 0 <= j < n and (i,j) not in seen and image[i][j] == image[x][y]:
                    seen.add((i,j))
                    answer[i][j] = newColor
                    points.append((i,j))
        return answer
        
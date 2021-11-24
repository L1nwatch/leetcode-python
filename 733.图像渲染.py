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

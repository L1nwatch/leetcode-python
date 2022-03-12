class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0]*n for i in range(n)]
        f[0][0] = triangle[0][0]

        for i in range(1,n):
            f[i][0] = f[i-1][0] + triangle[i][0]
            for j in range(1,i):
                f[i][j] = min(f[i-1][j],f[i-1][j-1]) + triangle[i][j]
            f[i][i] = f[i-1][i-1] + triangle[i][i]
        return min(f[n-1])

class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        f = [[0]*rows for _ in range(rows)]
        for i in range(rows):
            cols = len(triangle[i])
            for j in range(cols):
                if j == 0:
                    f[i][j] = f[i-1][j] + triangle[i][j]
                elif j == cols - 1:
                    f[i][j] = f[i-1][j-1] + triangle[i][j]
                else:
                    f[i][j] = min(f[i-1][j-1],f[i-1][j]) + triangle[i][j]
        return min(f[rows-1])
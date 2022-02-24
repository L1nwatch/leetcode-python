class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,columns = len(mat),len(mat[0])
        answer = [[0]*columns for _ in range(rows)]
        from collections import deque
        zeros = deque([(i,j) for i in range(rows) for j in range(columns) if mat[i][j] == 0])
        seen = set(zeros)

        while zeros:
            i,j = zeros.popleft()
            for new_i,new_j in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= new_i < rows and 0 <= new_j < columns and (new_i,new_j) not in seen:
                    answer[new_i][new_j] = answer[i][j] + 1
                    seen.add((new_i,new_j))
                    zeros.append((new_i,new_j))
        return answer

class Solution:
    # TLE
    def dfs(self,mat,i,j,depth):
        if mat[i][j] == 0:
            return depth
        next_point = list()
        for new_x,new_y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if 0 <= new_x < self.rows and 0 <= new_y < self.columns:
                if mat[new_x][new_y] == 0:
                    return depth + 1
                next_point.append((new_x,new_y))
        else:
            return min([self.dfs(mat,new_x,new_y,depth+1) for new_x,new_y in next_point])

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        answer = list()
        self.rows,self.columns = len(mat),len(mat[0])
        for i in range(self.rows):
            row_answer = list()
            for j in range(self.columns):
               row_answer.append(self.dfs(mat,i,j,0))
            answer.append(row_answer)
        return answer
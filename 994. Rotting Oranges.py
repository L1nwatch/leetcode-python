class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,columns = len(grid),len(grid[0])
        rotten_oranges,fresh_oranges = list(),0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    rotten_oranges.append((i,j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        raw_rotten = len(rotten_oranges)
        if raw_rotten == 0 and fresh_oranges == 0:
            return 0
        elif raw_rotten == 0:
            return -1
        elif raw_rotten == rows*columns:
            return 0

        from collections import deque
        rotten_oranges_deque = deque(rotten_oranges)
        seen = set(rotten_oranges)
        answer = 0

        while rotten_oranges_deque:
            answer += 1
            next_rottens = deque()
            while rotten_oranges_deque:
                i,j = rotten_oranges_deque.popleft()
                for ni,nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == 1 and (ni,nj) not in seen:
                        seen.add((ni,nj))
                        next_rottens.append((ni,nj))
            rotten_oranges_deque = next_rottens
        
        if len(seen) == fresh_oranges+raw_rotten:
            return answer - 1
        else:
            return -1      

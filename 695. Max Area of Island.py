class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        queue = list()
        rows,columns = len(grid),len(grid[0])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    queue.append((i,j))
        
        visited_set = set()
        for start_x,start_y in queue:
            if (start_x,start_y) in visited_set:
                continue

            area = 1
            island = list()
            island.append((start_x,start_y))   
            visited_set.add((start_x,start_y))
            while len(island) > 0:
                x,y = island.pop()
                for new_x,new_y in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0 <= new_x < rows and 0 <= new_y < columns and grid[new_x][new_y] == 1 and (new_x,new_y) not in visited_set:
                        visited_set.add((new_x,new_y))
                        island.append((new_x,new_y))
                        area += 1
            answer = max(answer,area)
        return answer

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        m,n = len(grid),len(grid[0])
        from collections import deque
        points = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        points = deque(points)
        seen = set()
        while points:
            x,y = points.pop()
            if (x,y) not in seen:
                area_deque = deque([(x,y)])
                area = 1
                seen.add((x,y))
                while area_deque:
                    x,y = area_deque.pop()
                    for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                        if 0 <= i < m and 0 <= j < n and grid[i][j] == 1 and (i,j) not in seen:
                            area += 1
                            area_deque.append((i,j))
                            seen.add((i,j))
                answer = max(area,answer)
        return answer
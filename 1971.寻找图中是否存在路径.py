#
# @lc app=leetcode.cn id=1971 lang=python3
#
# [1971] 寻找图中是否存在路径
#

# @lc code=start
class Solution:
    #DFS
    def common(self, n,source, destination,edges):
        if source == destination:
            return True
        
        adjacent = {key: list() for key in range(n)}
        for edge in edges:
            x,y = edge[0],edge[1]
            adjacent[x].append(y)
            adjacent[y].append(x)
        self.adjacent = adjacent
    
    def dfs(self,current_point):
        if current_point == self.destination:
            return True
        self.visited.add(current_point)
        for next_point in self.adjacent[current_point]:
            if next_point not in self.visited and self.dfs(next_point):
                return True
        return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        result = self.common(n,source,destination,edges)
        if result:
            return result
        self.visited = set()
        self.destination = destination
        return self.dfs(source)

        
    #BFS
    def BFS_validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        result = self.common(n,source,destination,edges)
        if result:
            return result

        visited = list()
        queue = [source]
        while len(queue) > 0:
            current_point = queue.pop(0)
            visited.append(current_point)
            for next_point in self.adjacent[current_point]:
                if next_point == destination:
                    return True
                elif next_point not in visited:
                    queue.append(next_point)
                
        return False


# @lc code=end


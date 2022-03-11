class Solution1:
    """
[1, 2, 3, 4]
[1, 2, 3]
[1, 2, 4]
[1, 2]
[1, 3, 4]
[1, 3]
[1, 4]
[1]
[2, 3, 4]
[2, 3]
[2, 4]
[2]
[3, 4]
[3]
[4]
[]
    """

    def dfs(self, cur, n, k):
        if cur == n + 1:
            print(self.answer)
            return
        self.answer.append(cur)
        self.dfs(cur + 1, n, k)
        self.answer.pop()
        self.dfs(cur + 1, n, k)

    def combine(self, n: int, k: int) -> list:
        self.answer = list()
        self.dfs(1, n, k)
        return self.answer


class Solution2:
    """
[1, 2]
[1, 3]
[1, 4]
[2, 3]
[2, 4]
[3, 4]
    """

    def dfs(self, cur, n, k):
        if len(self.answer) == k:
            print(self.answer)
            return

        if cur == n + 1:
            return
        self.answer.append(cur)
        self.dfs(cur + 1, n, k)
        self.answer.pop()
        self.dfs(cur + 1, n, k)

    def combine(self, n: int, k: int) -> list:
        self.answer = list()
        self.dfs(1, n, k)
        return self.answer


class Solution3:
    """
[1, 2]
[1, 3]
[1, 4]
[2, 3]
[2, 4]
[3, 4]
    """

    def dfs(self, cur, n, k):
        if len(self.temp) + n - cur + 1 < k:
            pass
        elif len(self.temp) == k:
            from copy import copy
            yield copy(self.temp)
        else:
            self.temp.append(cur)
            yield from self.dfs(cur + 1, n, k)
            self.temp.pop()
            yield from self.dfs(cur + 1, n, k)

    def combine(self, n: int, k: int) -> list:
        self.temp = list()
        answer = list(self.dfs(1, n, k))
        return answer


class Solution:

    def dfs(self, cur, n, k):
        if len(self.temp) + n - cur + 1 < k:
            return
        if len(self.temp) == k:
            import copy
            yield copy.copy(self.temp)
            return

        self.temp.append(cur)
        yield from self.dfs(cur + 1, n, k)
        self.temp.pop()

        yield from self.dfs(cur + 1, n, k)

    def combine(self, n: int, k: int) -> list:
        self.temp = list()
        return list(self.dfs(1, n, k))


class Solution4:
    def dfs(self,cur):
        if len(self.temp) + self.n - cur + 1 < self.k:
            return

        if len(self.temp) == self.k:
            import copy
            yield copy.copy(self.temp)
            return

        self.temp.append(cur)
        yield from self.dfs(cur+1)
        self.temp.pop()
        yield from self.dfs(cur+1)

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.k = k
        self.temp = list()       
        return list(self.dfs(1))

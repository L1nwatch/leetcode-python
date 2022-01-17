#
# @lc app=leetcode.cn id=1560 lang=python3
#
# [1560] 圆形赛道上经过次数最多的扇区
#

# @lc code=start
from typing import AnyStr


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        counter = {x: 0 for x in range(1, n+1)}
        counter[rounds[0]] += 1

        for i in range(1, len(rounds)):
            if rounds[i] > rounds[i-1]:
                for j in range(1, rounds[i]-rounds[i-1]+1):
                    counter[j+rounds[i-1]] += 1
            else:
                for j in range(1, rounds[i]+n-rounds[i-1]+1):
                    if (x := j+rounds[i-1]) <= n:
                        counter[x] += 1
                    else:
                        counter[x % n] += 1
        answer = list()
        max_times = max(counter.values())
        for key, value in counter.items():
            if value == max_times:
                answer.append(key)
        return sorted(answer)


# @lc code=end

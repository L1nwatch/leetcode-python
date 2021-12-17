#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        import heapq
        heapq.heapify(stones)
        while len(stones) >= 2:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x > y:
                heapq.heappush(stones, y-x)
        return 0 if len(stones) == 0 else -stones[0]

# @lc code=end
    def get_insert_index(self, stones: List[int], weight: int) -> int:
        low, high = 0, len(stones)-1
        while low < high:
            middle = low + (high-low)//2
            if stones[middle] == weight:
                return middle
            elif stones[middle] < weight:
                low = middle + 1
            elif stones[middle] > weight:
                high = middle
        if len(stones) == 0 or stones[low] > weight:
            return low
        else:
            return low + 1

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while len(stones) >= 2:
            y = stones.pop()
            x = stones.pop()
            if x != y:
                left_stone = y-x
                stones.insert(self.get_insert_index(
                    stones, left_stone), left_stone)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0

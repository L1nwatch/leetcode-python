class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = list()
        for num in nums:
            answer.append(num ** 2)
        return sorted(answer)
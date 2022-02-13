class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        answer = list()
        for num in nums:
            if num != lower:
                answer.append(f"{lower}->{num-1}" if num-1 != lower else f"{lower}")
                lower = num+1
            else:
                lower += 1
        if lower < upper:
            answer.append(f"{lower}->{upper}")
        elif lower == upper:
            answer.append(f"{lower}")
        return answer
            
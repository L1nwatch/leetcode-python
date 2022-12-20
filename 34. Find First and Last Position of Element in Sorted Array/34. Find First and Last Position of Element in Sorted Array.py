class Solution:
    def binary_search(self,nums,target:int,need_lower:bool) -> int:
        low,high = 0,self.length-1
        answer = self.length
        while low <= high:
            middle = low + (high-low)//2
            value = nums[middle]
            if value > target or (need_lower and value >= target):
                high = middle - 1
                answer = middle
            else:
                low = middle + 1
        return answer

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.length = len(nums)
        start = self.binary_search(nums,target,True)
        end = self.binary_search(nums,target,False)-1
        if start <= end and end < self.length and nums[start] == target and nums[end] == target:
            return [start,end]
        return [-1,-1]
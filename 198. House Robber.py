class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0]*n
        f[0] = nums[0]
        if n > 1:
            f[1] = max(nums[0],nums[1])        
        for i in range(2,n):
            f[i] = max(f[i-2]+nums[i],f[i-1])
        return f[n-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        f = [0]*length
        f[0] = nums[0]
        f[1] = max(nums[0],nums[1])
        for i in range(2,length):
            f[i] = max(f[i-1],f[i-2]+nums[i])
        return f[-1]

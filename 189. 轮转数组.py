class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length

        answer = nums[::-1]
        answer[:k] = answer[:k][::-1]
        answer[k:] = answer[k:][::-1]
        for i in range(length):
            nums[i] = answer[i]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        import math
        count = math.gcd(k,length)
        for start in range(count):
            current = start
            while True:
                next_item = (current + k)%length
                nums[start],nums[next_item] = nums[next_item],nums[start]
                current = next_item
                if start == current:
                    break
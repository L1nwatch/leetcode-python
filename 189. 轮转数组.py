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
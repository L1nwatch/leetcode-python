class Solution:
    # TLE
    def trap(self, height: List[int]) -> int:
        answer = 0
        left = right = 0
        length = len(height)
        while left < length:
            found = False
            while left < length and height[left] == 0:
                left += 1
            if left >= length:
                break
            max_height = (0,0)
            right = left + 1
            while right < length and height[right] < height[left]:
                if height[right] > max_height[0]:
                    max_height = (height[right], right)
                right += 1
            if right == length and left < length:
                right = max_height[1]
            i = left + 1
            while i < length and right < length and i < right:
                answer += min(height[right],height[left]) - height[i]
                i += 1
                found = True
            left = right if found else left+1
        return answer

class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        left,right = 0,len(height)-1
        left_max,right_max = 0,0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max,height[right])
            if height[left] < height[right]:
                answer += left_max - height[left]
                left += 1
            else:
                answer += right_max - height[right]
                right -= 1
        return answer
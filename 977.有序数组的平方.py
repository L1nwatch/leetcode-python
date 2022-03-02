class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = list()
        for num in nums:
            answer.append(num ** 2)
        return sorted(answer)

class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = list()
        for num in nums:
            answer.append(num**2)
        answer.sort()
        return answer
    
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0]*length
        i,j,pos = 0,length-1,length-1
        while i <= j:
            if (x:=nums[i]**2)>(y:=nums[j]**2):
                answer[pos] = x
                i += 1
            else:
                answer[pos] = y
                j -= 1
            pos -= 1
        return answer

class Solution4:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0]*n
        i,j,pos = 0,n-1,n-1
        while i <= j:

            if (x:=nums[i]**2) > (y:=nums[j] ** 2):
                answer[pos] = x
                i += 1
            else:
                answer[pos] = y
                j -= 1
            pos -= 1
        return answer
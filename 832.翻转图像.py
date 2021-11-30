#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        answer = list()
        for i in range(len(image)):
            temp = list()
            for num in image[i][::-1]:
                temp.append(num ^ 1)
            answer.append(temp)
        return answer
# @lc code=end


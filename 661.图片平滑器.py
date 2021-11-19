#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        answer = list()
        rows, cols = len(img), len(img[0])
        for i in range(rows):
            temp_i_list = list()
            answer.append(temp_i_list)
            for j in range(cols):
                value_sum = list()

                for x, y in [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]:
                    if x < 0 or x >= rows or y < 0 or y >= cols:
                        continue
                    value_sum.append(img[x][y])

                temp_i_list.append(sum(value_sum)//len(value_sum))
        return answer
# @lc code=end

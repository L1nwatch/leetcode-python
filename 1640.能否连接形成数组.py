#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#

# @lc code=start
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        result = list()
        result_index = 0
        length_arr = len(arr)

        for i in range(length_arr):
            if result_index < len(result):
                if result[result_index] != arr[i]:
                    return False
                else:
                    result_index += 1
                    continue

            for j in range(len(pieces)):
                if pieces[j][0] == arr[i]:
                    result.extend(pieces.pop(j))
                    result_index += 1
                    break
            else:
                return False
        return True

# @lc code=end

#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_1 = {key:value for value,key in enumerate(list1)}
        dict_2 = {key:value for value,key in enumerate(list2)}

        min_sum = 2001
        for each_key in list1:
            if each_key in dict_2:
                dict_1[each_key] += dict_2[each_key]
                min_sum = min(min_sum,dict_1[each_key])
            else:
                del dict_1[each_key]
        
        return [key for key,value in dict_1.items() if value == min_sum]
        

# @lc code=end


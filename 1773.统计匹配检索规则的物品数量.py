#
# @lc app=leetcode.cn id=1773 lang=python3
#
# [1773] 统计匹配检索规则的物品数量
#

# @lc code=start
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        answer = 0
        key_map = {
            "color":1,
            "type":0,
            "name":2
        }
        for item in items:
            if item[key_map[ruleKey]] == ruleValue:
                answer += 1
        return answer
# @lc code=end


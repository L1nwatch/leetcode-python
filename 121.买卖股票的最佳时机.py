#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0
        min_price = 10**6
        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            temp_value = prices[i]-min_price
            max_value = max(temp_value, max_value)
        return max_value
# @lc code=end
    # Time Limit Exceeded
        max_value = 0
        is_decrease_list = True
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                is_decrease_list = False

        if not is_decrease_list:
            max_price = max(prices)
            for i in range(len(prices)):
                if prices[i] == max_price and i < len(prices) - 1:
                    max_price = max(prices[i+1:])
                temp_value = max_price-prices[i]
                max_value = max(temp_value, max_value)
        return max_value

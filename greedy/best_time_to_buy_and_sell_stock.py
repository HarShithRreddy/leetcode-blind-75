"""
Problem: 121. Best Time to Buy and Sell Stock
Difficulty: Easy
Category: Sliding Window / Greedy

Approach:
- Traverse the price list once from left to right
- Track the minimum price seen so far (best day to buy)
- At each step, calculate the profit if sold on that day
- Update the maximum profit whenever a better profit is found

Time Complexity: O(n)
Space Complexity: O(1)

Note:
This solution maintains valid buy-before-sell order by only
comparing the current price with past minimum prices.
"""
class Solution:
    def maxProfit(self,prices):
        profit=0
        min=prices[0]
        for i in prices:
            if(i<min):
                min=i
            if(i-min>profit):
                profit=i-min
        return profit
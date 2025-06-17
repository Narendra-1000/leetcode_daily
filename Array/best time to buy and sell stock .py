"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0."""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        buy = prices[0]
        profit = 0
        for i in range(len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            if (prices[i] - buy) > profit and (prices[i] - buy) > 0:
                profit = max((prices[i] - buy), profit)
        return profit

"""
| i | prices\[i] | buy (min price so far) | prices\[i] - buy | profit (max profit so far) | Action        |
| - | ---------- | ---------------------- | ---------------- | -------------------------- | ------------- |
| 0 | 7          | 7                      | 0                | 0                          | init          |
| 1 | 1          | 1 (new low)            | 0                | 0                          | update buy    |
| 2 | 5          | 1                      | 4                | 4 (new max profit)         | update profit |
| 3 | 3          | 1                      | 2                | 4                          | no update     |
| 4 | 6          | 1                      | 5                | 5 (new max profit)         | update profit |
| 5 | 4          | 1                      | 3                | 5                          | no update     |
"""
"""
💡 Explanation:
You buy at the lowest point seen so far (buy).
At each day, you compute the potential profit: prices[i] - buy.
If it’s better than your current best (profit), you update it.
If a lower price is seen, you update your buy.
"""

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    profit = Solution().maxProfit(prices)
    print("Profit is : ",profit)

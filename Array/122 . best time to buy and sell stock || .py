"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time. However,
you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


"""
| Day | Price | Action                          | Profit So Far |
| --- | ----- | ------------------------------- | ------------- |
| 1   | 1     | ↓ from 7 → no profit            | 0             |
| 2   | 5     | ↑ from 1 → buy @1, sell @5 → +4 | 4             |
| 3   | 3     | ↓ from 5 → no profit            | 4             |
| 4   | 6     | ↑ from 3 → buy @3, sell @6 → +3 | 7             |
| 5   | 4     | ↓ from 6 → no profit            | 7             |
✅ Step-by-Step Explanation (For Quick Revision)
1. Initialize profit = 0
2. Loop from day 1 to end (i = 1 to len(prices)-1)
3. Compare today's price (prices[i]) with yesterday's price (prices[i-1])
4. If prices[i] > prices[i-1], that means:
    Buy yesterday
    Sell today
    Profit = prices[i] - prices[i-1]
    Add this to total profit
5. Why is this greedy approach valid?
    We capture every local increase as an opportunity
    It simulates buying low & selling high repeatedly
6. Return the accumulated profit
"""

# Test the solution
if __name__ == "__main__":
    sol = Solution()
    test_case = [7, 1, 5, 3, 6, 4]
    print("Max profit:", sol.maxProfit(test_case))


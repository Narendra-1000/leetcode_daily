"""Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

"""
| Step | num | candidate | count |
| ---- | --- | --------- | ----- |
| 1    | 2   | 2         | 1     |
| 2    | 2   | 2         | 2     |
| 3    | 1   | 2         | 1     |
| 4    | 1   | 2         | 0     |
| 5    | 1   | 1         | 1     |
| 6    | 2   | 1         | 0     |
| 7    | 2   | 2         | 1     |
"""
"""
✅ Step-by-Step Explanation (Revision Notes)
1. Initialize candidate = None, count = 0
2. Iterate over the array:
    If count == 0, choose candidate = num
    If num == candidate, increment count
    Else, decrement count
3. Return final candidate
4. ✅ Why it works:
    Majority element will cancel out all minority elements
    Since majority > ⌊n/2⌋, it survives at the end
✅ Time & Space Complexity
Time: O(n)
Space: O(1)
"""
# Example usage
if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = Solution().majorityElement(nums)
    print("Majority Element:", result)  # Output: Majority Element: 2

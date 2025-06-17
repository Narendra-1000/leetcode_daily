""""
Given an integer array nums, return the number of subarrays filled with 0.
A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation:
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9."""

from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res, count = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count = 0
            res += count
        return res
#TODO DRY RUN
"""
| i | nums\[i] | count (zeros till now) | res (total so far) |
| - | -------- | ---------------------- | ------------------ |
| 0 | 0        | 1                      | 1                  |
| 1 | 0        | 2                      | 3 (=1+2)           |
| 2 | 1        | 0                      | 3                  |
| 3 | 0        | 1                      | 4                  |
| 4 | 0        | 2                      | 6 (=4+2)           |
| 5 | 0        | 3                      | 9 (=6+3)           |
"""

"""
✅ Step-by-Step Explanation (Easy Revision)
1. Initialize two variables:
    res = 0 → stores total zero-filled subarrays
    count = 0 → tracks consecutive 0s
2. Loop through the list nums:
    If you find a 0, increment count by 1.
    If you find a non-zero, reset count to 0.
3. Why add count to res?
    Every time a 0 is added, new subarrays ending at this point are formed.
    e.g., 0 → 1 subarray
    0, 0 → 2 subarrays
    0, 0, 0 → 3 subarrays
Result Accumulation: 
Add count to res on each iteration, since it represents the number of new subarrays ending at this position.
Return the total res.
"""

# Test the solution
if __name__ == "__main__":
    sol = Solution()
    test_case = [0, 0, 1, 0, 0, 0]
    print("Total zero-filled subarrays:", sol.zeroFilledSubarray(test_case))

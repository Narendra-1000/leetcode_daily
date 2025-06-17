"""Given an integer array nums, move all 0 's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in -place without making a copy of the array.

Example
1:
Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
Example 2:

Input: nums = [0]
Output: [0]
https://leetcode.com/problems/move-zeroes/description/
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(0,len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
"""💡 Explanation:
1. We move all non-zero numbers to the front using the left pointer.
2. Each time we find a non-zero at right, we swap it with nums[left] and increment left.
3. This ensures that all zeroes get pushed toward the end without losing the order of non-zero elements.
"""

"""| Iteration | `right` | `nums[right]` | Condition `!= 0` | Swap (`nums[left]`, `nums[right]`) | `nums` after swap | `left` |
| --------- | ------- | ------------- | ---------------- | ---------------------------------- | ----------------- | ------ |
| 0         | 0       | 0             | ❌ False          | No swap                            | \[0, 1, 0, 3, 12] | 0      |
| 1         | 1       | 1             | ✅ True           | Swap `nums[0]` and `nums[1]`       | \[1, 0, 0, 3, 12] | 1      |
| 2         | 2       | 0             | ❌ False          | No swap                            | \[1, 0, 0, 3, 12] | 1      |
| 3         | 3       | 3             | ✅ True           | Swap `nums[1]` and `nums[3]`       | \[1, 3, 0, 0, 12] | 2      |
| 4         | 4       | 12            | ✅ True           | Swap `nums[2]` and `nums[4]`       | \[1, 3, 12, 0, 0] | 3      |
"""


def moveZeroes(nums: List[int]) -> None:
    """
    Moves all 0s to the end while keeping the order of non-zero elements.
    Modifies the list in-place.
    """
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(0)
            nums.remove(nums[i])

# Example usage
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    print(nums)  # Output: [1, 3, 12, 0, 0]

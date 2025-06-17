from typing import List

class Solution:
    def productOfArrayExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]

        suffix = [1] * n
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]

        output = [1] * n
        for i in range(0,n):
            output[i] = prefix[i] * suffix[i]

        return output

if __name__ == "__main__":
    nums = [1,2,3,4]
    nums_2 = [1,-1,0,-9,9]
    result = Solution().productOfArrayExceptSelf(nums_2)
    print("Product array except itself:",result)

"""
Step 1: Compute prefix array
Each prefix[i] = product of all elements before index i
| i | nums\[i] | prefix\[i] |
| - | -------- | ---------- |
| 0 | 1        | 1          |
| 1 | -1       | 1×1 = 1    |
| 2 | 0        | 1×-1 = -1  |
| 3 | -9       | -1×0 = 0   |
| 4 | 9        | 0×-9 = 0   |
➡️ prefix = [1, 1, -1, 0, 0]

Step 2: Compute suffix array
Each suffix[i] = product of all elements after index i
| i | nums\[i] | suffix\[i] |
| - | -------- | ---------- |
| 4 | 9        | 1          |
| 3 | -9       | 1×9 = 9    |
| 2 | 0        | 9×-9 = -81 |
| 1 | -1       | -81×0 = 0  |
| 0 | 1        | 0×-1 = 0   |


➡️ suffix = [0, 0, -81, 9, 1]

Step 3: Compute final output[i] = prefix[i] * suffix[i]
| i | prefix\[i] | suffix\[i] | output\[i] = prefix × suffix |
| - | ---------- | ---------- | ---------------------------- |
| 0 | 1          | 0          | 0                            |
| 1 | 1          | 0          | 0                            |
| 2 | -1         | -81        | 81                           |
| 3 | 0          | 9          | 0                            |
| 4 | 0          | 1          | 0                            |


➡️ ✅ Final Output: [0, 0, 81, 0, 0]
"""

"""
✅ Step-by-Step Explanation (For Revision)
1. Goal: Find product of all elements except the current index without using division.
2. Idea: Use two passes:
    prefix[i]: product of elements before index i
    suffix[i]: product of elements after index i
3. Initialize arrays:
    prefix = [1] * n
    suffix = [1] * n
4. Left-to-right pass → fill prefix
    prefix[i] = prefix[i-1] * nums[i-1]
5. Right-to-left pass → fill suffix
    suffix[i] = suffix[i+1] * nums[i+1]
6. Final output:
    output[i] = prefix[i] * suffix[i]
7. Time Complexity: O(n)
    Space Complexity: O(n) (can be reduced to O(1) if output reused)
"""


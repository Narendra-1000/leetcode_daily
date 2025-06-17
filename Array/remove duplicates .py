class Solution:
    def removeDuplicates(self, nums):
        # Check if the list is empty
        if len(nums) == 0:
            return 0

        # Initialize the pointer for unique elements
        i = 0

        # Iterate through the list starting from the second element
        for j in range(1, len(nums)):
            # If current element is different from the last unique element
            if nums[j] != nums[i]:
                # Move the pointer for unique elements and update the list
                i += 1
                nums[i] = nums[j]

        # Return the length of the list with unique elements
        return i + 1

"""
| Step | j | nums\[j] | i (last unique index) | nums                |
| ---- | - | -------- | --------------------- | ------------------- |
| init | - | -        | 0                     | \[1, 1, 2, 2, 3, 4] |
| 1    | 1 | 1        | 0 (same as nums\[i])  | \[1, 1, 2, 2, 3, 4] |
| 2    | 2 | 2        | 1 → nums\[1] = 2      | \[1, 2, 2, 2, 3, 4] |
| 3    | 3 | 2        | 1 (same as nums\[i])  | \[1, 2, 2, 2, 3, 4] |
| 4    | 4 | 3        | 2 → nums\[2] = 3      | \[1, 2, 3, 2, 3, 4] |
| 5    | 5 | 4        | 3 → nums\[3] = 4      | \[1, 2, 3, 4, 3, 4] |
🔹 Final i = 3
🔹 Return i + 1 = 4
✅ Updated list: [1, 2, 3, 4]
"""
"""
✅ Step-by-Step Explanation (For Revision)
1. ✅ Sorted input means duplicates are grouped together.
2. Two-pointer approach:
    i = last unique element index
    j = iterator over array
3. For every nums[j] != nums[i], increment i and assign nums[i] = nums[j].
4. Final length of unique list is i + 1
✅ Time & Space Complexity
Time: O(n) — single pass
Space: O(1) — in-place
"""

if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 4]
    solution = Solution()
    new_length = solution.removeDuplicates(nums)

    # Output the updated list and its new length
    print("Updated list:", nums[:new_length])
    print("New length:", new_length)

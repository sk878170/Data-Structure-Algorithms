from typing import List

class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Handle empty list case
        i = 0  # Pointer for the position of unique elements
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # If a new unique element is found
                i += 1
                nums[i] = nums[j]  # Move the unique element to the correct position
        return i + 1  # Return the count of unique elements

# Test the Solution
solution = Solution()
print("Enter numbers separated by spaces (sorted array):")
nums = list(map(int, input().split()))  # Input a sorted list
result = solution.remove_duplicates(nums)
print("Number of unique elements:", result)
print("Modified array with unique elements:", nums[:result])

from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for num in nums:
            if i<1 or num>nums[i-1]:
                nums[i] = num
                i += 1
        return i + 1

# Test the Solution
solution = Solution()
print("Enter numbers sepearted by spaces")
nums =list(map(int, input().split()))
result=solution.remove_duplicates(nums)
print(result)
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        i = 1
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 1]:
                i += 1
                nums[i] = nums[j]
        return i + 1
    
nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 2, 1]
solution = Solution()
result = solution.removeDuplicates(nums)
print("Length of modified array:", result)
print("Modified array:", nums[:result])

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return len(nums)
        i = 2
        for j in range(3, len(nums)):
            if nums[j] != nums[i - 2]:
                i += 1
                nums[i] = nums[j]
        return i + 1
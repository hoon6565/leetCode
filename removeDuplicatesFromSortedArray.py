class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] == nums[index]:
                continue
            else:
                index += 1
                nums[index] = nums[i]
        return index + 1
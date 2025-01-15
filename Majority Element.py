class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        for item in nums:
            count_dict[item] = count_dict.get(item, 0) + 1
        max_key = max(count_dict, key=count_dict.get)
        return max_key
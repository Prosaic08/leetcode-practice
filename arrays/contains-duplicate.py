"""I compared the length of the set of nums to the length of actual nums list"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
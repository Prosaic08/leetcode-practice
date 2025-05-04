

"""My first thought process was to loop through
each index of the list. I realized that this method would be ineffient since its O(n^2)"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[j] + nums[i] == target:
                    answer = [i, j]
                j += 1
            i += 1
        return answer
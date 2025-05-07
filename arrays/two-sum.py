"""First, create an empty hashmap to store elements and their indices in nums.
Loop through the nums list and calculate the difference between the target
and the current element. Next, check if this difference is already in the hashmap.
If it is, return the index of the difference from the hashmap and the current index.
 Otherwise, add the current element and its index to the hashmap."""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} #val = index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in d:
                return [d[diff], i]
            d[n] = i
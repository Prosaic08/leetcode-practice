"""Turn nums into a set to allow O(1) lookups.  
Initialize a variable to track the longest consecutive sequence.  
Loop through the set and only start counting when the current number is
the beginning of a sequence (i.e., num - 1 is not in the set).  
Expand the sequence by checking if num + 1, num + 2, etc. are in the set, and update the longest length found.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in nums:
                    length += 1
                longest = max(length, longest)
        return longest
"""made a duplicate list which is empty. I looped through nums. For every index,
I would append it to the duplicate list that Ive seen so far.
If value was already in duplicate, then would return True.
If loop finishes without finding any duplicates, return False"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = []
        for i in nums:
            if i in duplicate:
                return True
            else:
                duplicate.append(i)
        return False
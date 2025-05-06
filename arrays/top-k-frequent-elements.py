"""I created a hashap to link the numbers in the list to the frequency.
sorted the dictionaries based on the values. I returned the keys using
the slicing method."""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #key=num
        #value=frequency
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        d = sorted(d, key=d.get, reverse=True)
        return d[:k]
"""I created a prefix list that stores the product of all elements that come
before index i. Then, I do a second pass from the end of the array, using a postfix
 value that represents the product of all elements after index i.
For each position, I multiply the prefix value already stored with the current 
postfix, and update the result. This way, each index ends up with the product 
of everything except itself, since both the prefix and postfix skip
over i naturally — prefix stops just before i, and postfix starts just after i."""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        #calculating product of all elements before i and putting them in res
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        #calculating product of all elements after i and multiplying in res
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
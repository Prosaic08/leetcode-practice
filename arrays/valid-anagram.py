"""First, we compare the lengths of the two strings. If they are not the same, we return false. 
We then create two hashmaps to count the letters in each string. If the two dictionaries are the same, 
we return true; otherwise, we return false. In time complexity this solution is O(n+m)
however solution may take too  much memory space depending on the length of the input strings."""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            sMap, tMap = {}, {}
            for i in s:
                sMap[i] = sMap.get(i, 0) + 1
            for i in t:
                tMap[i] = tMap.get(i, 0) + 1
            return sMap == tMap

"""First I compared the length of the two words, if not, they arent anagrams. Then
I went through each character in the first word. If count of that character is not the 
same in both words, its not an anagram, if they match, they are anagrams."""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for i in s:
                if s.count(i) != t.count(i):
                    return False
            return True
        return False
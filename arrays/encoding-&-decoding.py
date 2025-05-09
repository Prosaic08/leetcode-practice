"""To encode a list into a string, we need a delimiter to separate strings in the list. 
We also include the length of each string before the delimiter. This helps ensure we can retrieve each part of the string accurately during decoding.

To decode it, we use a pointer j to read until the delimiter and another pointer i to track our position in the string. 
First, we extract the length of the string using slicing, then append the next length characters to the list. We update i and repeat the process."""

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return res

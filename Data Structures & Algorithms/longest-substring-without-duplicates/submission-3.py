class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newW = ""
        newS = 0
        for char in s:
            if char in newW:
                newW = newW[newW.index(char) + 1:]
            newW += char
            newS = max(newS, len(newW))
        return newS
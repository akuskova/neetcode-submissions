class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countMaps = {}
        countMapt = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countMaps[s[i]] = 1 + countMaps.get(s[i], 0)
            countMapt[t[i]] = 1 + countMapt.get(t[i], 0)

        return countMaps == countMapt
        


        
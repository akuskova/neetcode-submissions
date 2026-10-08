class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
    

        for i in range(len(s2)):
            if Counter(s2[i:i+len(s1)]) == count: return True

        return False



        
        
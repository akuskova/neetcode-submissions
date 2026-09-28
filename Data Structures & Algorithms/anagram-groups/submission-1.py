class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list) 
        for s in strs:
            letters = [0]*26
            for chara in s:
                letters[ord(chara)-ord('a')] += 1 
            anag[tuple(letters)].append(s)
        return list(anag.values())
        
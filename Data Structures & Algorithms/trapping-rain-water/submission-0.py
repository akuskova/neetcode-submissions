class Solution:
    def trap(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        maxL, maxR = height[i], height[j]
        depth = 0
        while i < j:
            if maxL < maxR:
                i += 1
                maxL = max(height[i], maxL)
                depth += max(0, maxL - height[i])
            else:
                j -= 1
                maxR = max(height[j], maxR)
                depth += max(0, maxR - height[j])
        
        return depth